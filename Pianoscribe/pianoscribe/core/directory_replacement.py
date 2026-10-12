from __future__ import annotations

from contextlib import contextmanager
import os
import errno
from pathlib import Path
import re
import threading
import time
import uuid

_LOCKS: dict[str, threading.Lock] = {}
_LOCKS_GUARD = threading.Lock()


@contextmanager
def installation_lock(target: Path, stop_event=None):
    target = Path(target).resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    with _LOCKS_GUARD:
        lock = _LOCKS.setdefault(os.path.normcase(str(target)), threading.Lock())
    while not lock.acquire(timeout=.1):
        _check_stop(stop_event)
    stream = None
    acquired = False
    try:
        _check_stop(stop_event)
        stream = (target.parent / f'.lock-{target.name}').open('a+b')
        if stream.seek(0, os.SEEK_END) == 0:
            stream.write(b'\0')
            stream.flush()
        while not acquired:
            _check_stop(stop_event)
            stream.seek(0)
            try:
                if os.name == 'nt':
                    import msvcrt
                    msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                acquired = True
            except OSError as exc:
                if exc.errno not in (errno.EACCES, errno.EAGAIN, errno.EDEADLK):
                    raise
                time.sleep(.1)
        yield
    finally:
        try:
            if stream is not None:
                try:
                    if acquired:
                        stream.seek(0)
                        if os.name == 'nt':
                            import msvcrt
                            msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
                        else:
                            import fcntl
                            fcntl.flock(stream.fileno(), fcntl.LOCK_UN)
                finally:
                    stream.close()
        finally:
            lock.release()


def _check_stop(stop_event):
    if stop_event is not None and stop_event.is_set():
        raise InterruptedError('Installation was stopped.')


def _valid(path, validate):
    if not path.is_dir():
        return False
    try:
        validate(path)
        return True
    except Exception:
        return False


def _cleanup(path):
    from .archive_service import remove_tree
    try:
        remove_tree(path)
    except OSError:
        pass


def recover_directory(target: Path, validate) -> bool:
    target = Path(target)
    backup = target.parent / f'.backup-{target.name}'
    if _valid(target, validate):
        if backup.exists():
            _cleanup(backup)
        return True
    candidate = backup if _valid(backup, validate) else None
    if candidate is None:
        legacy = [p for p in target.parent.glob(f'.backup-{target.name}-*')
                  if re.fullmatch(rf'\.backup-{re.escape(target.name)}-[0-9a-fA-F]{{32}}', p.name)
                  and _valid(p, validate)]
        if len(legacy) > 1:
            raise RuntimeError(f'Ambiguous interrupted installation backups for {target.name}; backups were preserved.')
        candidate = legacy[0] if legacy else None
    if candidate is None:
        return False
    if target.exists():
        target.replace(target.parent / f'.invalid-{target.name}-{uuid.uuid4().hex}')
    candidate.replace(target)
    validate(target)
    return True


def replace_directory(stage: Path, target: Path, validate, stop_event=None) -> Path:
    recover_directory(target, validate)
    validate(stage)
    _check_stop(stop_event)
    backup = target.parent / f'.backup-{target.name}'
    if backup.exists():
        backup.replace(target.parent / f'.preserved-{target.name}-{uuid.uuid4().hex}')
    if target.exists():
        if _valid(target, validate):
            target.replace(backup)
        else:
            target.replace(target.parent / f'.invalid-{target.name}-{uuid.uuid4().hex}')
    try:
        _check_stop(stop_event)
        stage.replace(target)
        validate(target)
    except Exception:
        recover_directory(target, validate)
        raise
    if backup.exists():
        _cleanup(backup)
    return target
