from __future__ import annotations

import ast
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CudaRuntimeRequirements:
    ort_version: str
    cuda_majors: tuple[int, ...]
    cudnn_major: int


def read_build_metadata(source: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for node in ast.parse(source).body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in {'__version__', 'cuda_version', 'package_name'}:
                    value = ast.literal_eval(node.value)
                    if not isinstance(value, str):
                        raise ValueError(f'Invalid literal build identity: {target.id}')
                    if target.id in values and values[target.id] != value:
                        raise ValueError(f'Conflicting build identity: {target.id}')
                    values[target.id] = value
    return values


def requirements_for_build(ort_version: str, *, cuda_version: str = '', cudnn_major: int | None = None) -> CudaRuntimeRequirements:
    raw_parts = str(ort_version).replace('-', '.').split('.')
    parts = []
    for part in raw_parts:
        if not part.isdigit():
            break
        parts.append(int(part))
        if len(parts) == 3:
            break
    version = tuple((parts + [0, 0, 0])[:3])
    default_cuda = 13 if version >= (1, 27, 0) else 12 if version >= (1, 17, 0) else 11
    default_cudnn = 9 if version >= (1, 18, 1) else 8
    if cuda_version:
        tokens = str(cuda_version).split('.')
        if not all(token.isdigit() for token in tokens) or int(tokens[0]) not in (11, 12, 13):
            raise ValueError(f'Unsupported CUDA build version: {cuda_version}')
        default_cuda = int(tokens[0])
    selected_cudnn = default_cudnn if cudnn_major is None else int(cudnn_major)
    if selected_cudnn not in (8, 9):
        raise ValueError(f'Unsupported cuDNN major: {selected_cudnn}')
    return CudaRuntimeRequirements(str(ort_version), (default_cuda,), selected_cudnn)
