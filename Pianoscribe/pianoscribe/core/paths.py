from __future__ import annotations
import os
import sys
from collections.abc import Iterable
from pathlib import Path
from .config import APP_SHORT_NAME, CONFIG_FILENAME, LEGACY_APP_SHORT_NAME, LEGACY_CONFIG_FILENAME

def app_root_dir() -> Path:
    return Path(__file__).resolve().parents[2]

def app_dir() -> Path:
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).resolve().parent
    return app_root_dir()

def bundle_dir() -> Path:
    if getattr(sys, 'frozen', False):
        base = getattr(sys, '_MEIPASS', None)
        if base:
            return Path(base)
    return app_dir()

def icon_path() -> Path:
    bundled = bundle_dir() / 'icon.ico'
    if bundled.exists():
        return bundled
    local = app_dir() / 'icon.ico'
    if local.exists():
        return local
    return bundled

def product_data_dir() -> Path:
    return localappdata_dir() / APP_SHORT_NAME

def legacy_product_data_dirs() -> list[Path]:
    return [localappdata_dir() / LEGACY_APP_SHORT_NAME]

def _move_path_if_possible(source: Path, destination: Path) -> bool:
    try:
        if not source.exists() or destination.exists():
            return False
        destination.parent.mkdir(parents=True, exist_ok=True)
        source.replace(destination)
        return True
    except OSError:
        return False

def migrate_legacy_product_data() -> None:
    primary = product_data_dir()
    for legacy in legacy_product_data_dirs():
        if not legacy.exists():
            continue
        if _move_path_if_possible(legacy, primary):
            break
        for child_name in ('models', 'runtime_packs', 'dependencies'):
            _move_path_if_possible(legacy / child_name, primary / child_name)

    _move_path_if_possible(
        primary / LEGACY_CONFIG_FILENAME,
        primary / CONFIG_FILENAME,
    )

def remap_legacy_product_path(value: Path | str) -> Path:
    candidate = Path(value)
    for legacy_root in legacy_product_data_dirs():
        try:
            relative = candidate.relative_to(legacy_root)
        except ValueError:
            continue
        mapped = product_data_dir() / relative
        if mapped.exists() or not candidate.exists():
            return mapped
        return candidate
    return candidate

def config_path() -> Path:
    migrate_legacy_product_data()
    return product_data_dir() / CONFIG_FILENAME

def legacy_config_paths() -> list[Path]:
    appdata = os.environ.get('APPDATA')
    roaming_root = Path(appdata) if appdata else Path.home() / 'AppData' / 'Roaming'
    return dedupe_paths(
        (
            app_dir() / CONFIG_FILENAME,
            app_dir() / LEGACY_CONFIG_FILENAME,
            roaming_root / 'Pianoscribe' / CONFIG_FILENAME,
            localappdata_dir() / LEGACY_APP_SHORT_NAME / LEGACY_CONFIG_FILENAME,
            roaming_root / LEGACY_APP_SHORT_NAME / LEGACY_CONFIG_FILENAME,
            Path.home() / '.pianoscribe_config.json',
            Path.home() / '.a2m_config.json',
        ),
        resolve_if_exists=False,
    )

def localappdata_dir() -> Path:
    root = os.environ.get('LOCALAPPDATA')
    if root:
        return Path(root)
    return Path.home() / 'AppData' / 'Local'


def normalized_path_key(path: Path | str, *, resolve_if_exists: bool=True) -> str:
    candidate = Path(path)
    try:
        if resolve_if_exists and candidate.exists():
            return str(candidate.resolve()).lower()
    except Exception:
        pass
    return str(candidate).strip().lower()


def dedupe_paths(paths: Iterable[Path | str], *, existing_only: bool=False, resolve_if_exists: bool=True) -> list[Path]:
    deduped: list[Path] = []
    seen: set[str] = set()
    for raw in paths:
        candidate = Path(raw)
        if not str(candidate):
            continue
        if existing_only and (not candidate.exists()):
            continue
        key = normalized_path_key(candidate, resolve_if_exists=resolve_if_exists)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(candidate)
    return deduped
