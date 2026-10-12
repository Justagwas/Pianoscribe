from __future__ import annotations
from pathlib import Path

APP_NAME = 'Pianoscribe'
APP_SHORT_NAME = 'Pianoscribe'
APP_VERSION = '3.1.0'
APP_RESTART_EXIT_CODE = 75
OFFICIAL_PAGE_URL = 'https://www.justagwas.com/projects/pianoscribe/download'
DONATE_PAGE_URL = 'https://www.justagwas.com/donate'
CONFIG_FILENAME = 'pianoscribe_config.json'
LEGACY_APP_SHORT_NAME = 'A2M'
LEGACY_CONFIG_FILENAME = 'a2m_config.json'
INNO_SETUP_APP_ID = 'PianoscribeJustagwas'
CONFIG_SCHEMA_VERSION = 7
GPU_BATCH_SIZE_MIN = 1
GPU_BATCH_SIZE_MAX = 16
UI_SCALE_PERCENT_MIN = 75
UI_SCALE_PERCENT_MAX = 200
ENGINE_UNIFORM_VELOCITY_MIN = 1
ENGINE_UNIFORM_VELOCITY_MAX = 127
ENGINE_UNIFORM_VELOCITY_DEFAULT = 96
MODEL_URL = 'https://downloads.justagwas.com/pianoscribe/PianoModel.pianoscribe'
MODEL_FILENAME = 'PianoModel.pianoscribe'
MODEL_ID = 'pianoscribe-piano'
MODEL_VERSION = '1.0.1'
MODEL_SCHEMA_VERSION = 1
MODEL_INSTALL_DIRNAME = 'piano-engine'
MODEL_MIN_BYTES = 40 * 1024 * 1024
MODEL_SIZE_BYTES = 50795183
MODEL_SHA256 = 'bd7c3835288100e07ab4433ec690539685496790d1cba42e66501b36c6a85790'
MODEL_DOWNLOAD_MAX_BYTES = 100 * 1024 * 1024
UPDATE_MANIFEST_URL = 'https://www.justagwas.com/projects/pianoscribe/latest.json'
UPDATE_SETUP_FALLBACK_URL = 'https://downloads.justagwas.com/pianoscribe/PianoscribeSetup.exe'
UPDATE_CHECK_TIMEOUT_SECONDS = 12
CUDA_DOWNLOAD_URL = 'https://developer.nvidia.com/cuda-downloads'
CUDNN_DOWNLOAD_URL = 'https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/windows-x86_64/cudnn-windows-x86_64-9.19.0.56_cuda12-archive.zip'
CUDNN_DOWNLOAD_SHA256 = '03e1be06d7400f1fdc1ae2a5c82420d49d398cd252450b8d66ba5b9e2f502f08'
CUDNN_DOWNLOAD_SIZE = 634971654
CUDNN_DOWNLOAD_MAX_BYTES = 2 * 1024 * 1024 * 1024
CUDNN_CUDA13_DOWNLOAD_URL = 'https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/windows-x86_64/cudnn-windows-x86_64-9.19.0.56_cuda13-archive.zip'
CUDNN_CUDA13_DOWNLOAD_SHA256 = '49118983fe6230da71db1c1356ea2681d83e7404b4d828e19ab5f56ed3be8abd'
CUDNN_CUDA13_DOWNLOAD_SIZE = 349631454
ONNX_CUDA_RUNTIME_PACK_URL = 'https://downloads.justagwas.com/pianoscribe/pianoscribe-onnx-cuda.zip'
ONNX_CUDA_RUNTIME_PACK_SHA256 = '1fff99c96fb9cd6ff0fc3646b55219bb13965385ae04830e233f86488690764c'
ONNX_CUDA_RUNTIME_PACK_DOWNLOAD_SIZE = 212573446
ONNX_CUDA_RUNTIME_PACK_INSTALLED_SIZE = 280733225
ONNX_CUDA_RUNTIME_PACK_MAX_BYTES = 512 * 1024 * 1024
ONNX_CUDA_RUNTIME_PACK_ORT_VERSION = '1.27.0'
ONNX_DML_RUNTIME_PACK_URL = 'https://downloads.justagwas.com/pianoscribe/pianoscribe-onnx-dml.zip'
ONNX_DML_RUNTIME_PACK_SHA256 = 'd7caca61af606a388479a77d53bc9c0e03e06b89054eebeff04b31f9e61f7270'
ONNX_DML_RUNTIME_PACK_DOWNLOAD_SIZE = 24078577
ONNX_DML_RUNTIME_PACK_INSTALLED_SIZE = 66614960
ONNX_DML_RUNTIME_PACK_MAX_BYTES = 128 * 1024 * 1024
ONNX_DML_RUNTIME_PACK_ORT_VERSION = '1.24.4'
ARCHIVE_EXTRACT_MAX_BYTES = 3 * 1024 * 1024 * 1024
DOWNLOAD_TIMEOUT_SECONDS = 45
DOWNLOAD_RETRIES_PER_HEADER = 3
DOWNLOAD_RETRY_BACKOFF_SECONDS = 1.2
DOWNLOAD_HEADER_PROFILES = (
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'https://justagwas.com/',
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Accept': '*/*',
        'Referer': 'https://justagwas.com/',
    },
    {
        'User-Agent': f'{APP_SHORT_NAME}/{APP_VERSION}',
        'Accept': '*/*',
    },
)
DOWNLOADS_DIR = Path.home() / 'Downloads'
OUTPUT_MIDI_DIR = DOWNLOADS_DIR / 'Pianoscribe'
SUPPORTED_AUDIO_FILTER = 'Audio Files (*.mp3 *.wav *.flac *.ogg *.m4a *.aac *.wma *.aiff *.aif);;All Files (*.*)'
