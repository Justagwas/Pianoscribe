# Pianoscribe

<div align="center">

[![Code: GitHub](https://img.shields.io/badge/Code-GitHub-111827.svg?style=flat&logo=github&logoColor=white)](https://github.com/Justagwas/Pianoscribe)
[![Website](https://img.shields.io/badge/Website-Pianoscribe-0ea5e9.svg?style=flat&logo=google-chrome&logoColor=white)](https://www.justagwas.com/projects/pianoscribe/)
[![Mirror: SourceForge](https://img.shields.io/badge/Mirror-SourceForge-ff6600.svg?style=flat&logo=sourceforge&logoColor=white)](https://sourceforge.net/projects/pianoscribe/)

</div>

<p align="center">
  <img
    width="128"
    height="128"
    alt="Pianoscribe Logo"
    src="Pianoscribe/icon.ico"
  />
</p>

<div align="center">

[![Download (Windows)](https://img.shields.io/badge/Download-Windows%20(PianoscribeSetup.exe)-2563eb.svg?style=flat&logo=windows&logoColor=white)](https://github.com/Justagwas/Pianoscribe/releases/latest/download/PianoscribeSetup.exe)

</div>

<p align="center"><b>Turn piano recordings into editable MIDI</b></p>

<p align="center">Private local transcription with adjustable performance settings and optional graphics card acceleration</p>

<div align="center">

[![Version](https://img.shields.io/github/v/tag/Justagwas/Pianoscribe.svg?label=Version)](https://github.com/Justagwas/Pianoscribe/tags)
[![License](https://img.shields.io/github/license/Justagwas/Pianoscribe.svg)](https://github.com/Justagwas/Pianoscribe/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Justagwas/Pianoscribe/main.svg?style=flat&cacheSeconds=3600)](https://github.com/Justagwas/Pianoscribe/commits/main)
[![Open Issues](https://img.shields.io/github/issues/Justagwas/Pianoscribe.svg)](https://github.com/Justagwas/Pianoscribe/issues)
[![Stars](https://img.shields.io/github/stars/Justagwas/Pianoscribe.svg?style=flat&cacheSeconds=3600)](https://github.com/Justagwas/Pianoscribe/stargazers)
![Downloads (7d)](https://img.shields.io/badge/dynamic/json?style=flat&url=https%3A%2F%2Fdownload-stats-worker.justagwas.workers.dev%2Fdownloads%2Fpianoscribe%3Frange%3Dweek&query=%24.data.weekly.all&label=Downloads%20(7d))

</div>

## Overview

Pianoscribe turns piano recordings into **MIDI, a file of musical notes you can edit and arrange** in music or notation software. Use it to preserve an improvised idea, study a passage, or build an arrangement from a recorded performance.

This piano audio-to-MIDI converter runs locally on Windows without uploading your recording for analysis. It estimates notes, timing, dynamics, and optional pedal use. Clear solo piano recordings give it the best starting point.

## Features

- **Editable piano transcription:** note timing and strength, with optional sustain and soft-pedal events.
- **Output choices:** estimated note dynamics or a uniform strength for every note, with pedals included or omitted.
- **Local processing:** audio is analyzed on your computer; no recording upload is needed.
- **Resource controls:** Low, Balanced, High, and Max CPU settings, plus GPU memory settings on supported hardware.
- **Optional GPU acceleration:** CUDA or DirectML processing with compatible hardware and additional components.
- **Audio format support:** MP3, WAV, FLAC, OGG, M4A, AAC, WMA, AIFF, and AIF when a suitable decoder is available.
- **Safe output naming:** a chosen save folder and numbered filenames that preserve existing MIDI files.

## Basic usage

1. Get the [Windows installer or standalone app](https://www.justagwas.com/projects/pianoscribe/). Choose the installer for a normal setup, or standalone to run without installing.
2. Launch Pianoscribe and allow the required piano model to download when prompted.
3. Select **Choose Audio** and open a clear solo piano recording.
4. In **Settings**, choose **Expressive** to keep estimated differences in note strength, or **Uniform** to give every note the same strength. Choose whether to include **Pedal events**.
5. Select **Convert to MIDI**. CPU mode works without a graphics card setup; adjust resource settings if needed.
6. Select **Open output folder** and open the finished MIDI in your music software. Listen through it and correct notes, timing, or pedals where needed.

Default output folder: `%USERPROFILE%\Downloads\Pianoscribe`. Change it under **Settings > Output Location**. New results use numbered filenames when a name is already taken.

## Processing and setup

The official Windows installer and standalone app include CPU transcription support and do not need a separate Python installation. Both require the piano model download before their first conversion. Settings, the model, and managed GPU components normally stay in `%LOCALAPPDATA%\Pianoscribe`; moving the standalone executable does not move them with it.

**CPU usage** controls how many processor threads Pianoscribe uses. Lower settings leave more processing capacity for other work; higher settings allow more resources for transcription. These presets are not a fixed percentage in Windows Task Manager.

Optional **CUDA** or **DirectML** processing uses a compatible graphics card. GPU mode requires additional components and may require a restart. It runs the same transcription model; the speed benefit depends on the computer, recording, and settings. See the [CPU and GPU setup guide](https://github.com/Justagwas/Pianoscribe/wiki/CPU-and-GPU-Acceleration).

You can stop a conversion. Cancellation takes effect between processing steps, so the current operation may need a moment to finish.

## Understanding the result

MIDI contains musical notes and controller events, not the original recorded piano sound. You can edit it in music software or import it into notation software to prepare a score. Pianoscribe does not export a finished sheet-music document.

The transcription is an estimate. Reverb, background instruments, and overlapping notes can make a performance harder to interpret. The [worked example](https://github.com/Justagwas/Pianoscribe/wiki/Results-and-Validation) includes its audio, output MIDI, and comparison method so you can inspect one result. It was made with Pianoscribe v3.0.1 and does not establish an accuracy score for every recording.

Pianoscribe analyzes overlapping sections of the recording, estimates notes and pedals, refines their timing and dynamics, and joins them on one timeline. The [technical guide](https://github.com/Justagwas/Pianoscribe/wiki/How-Pianoscribe-Works) explains that process in detail.

## Project resources

- Project page: <https://www.justagwas.com/projects/pianoscribe/>
- Download page: <https://www.justagwas.com/projects/pianoscribe/download/>
- Documentation: <https://github.com/Justagwas/Pianoscribe/wiki>
- Releases: <https://github.com/Justagwas/Pianoscribe/releases>

<details>
<summary>For Developers</summary>

### Requirements

- Windows (primary runtime target).
- Python 3.12 or later.
- Dependencies in [`Pianoscribe/requirements.txt`](https://github.com/Justagwas/Pianoscribe/blob/main/Pianoscribe/requirements.txt).

### Running From Source

```powershell
cd Pianoscribe
py -m pip install -r requirements.txt
py Pianoscribe.py
```

### Configuration Files

- Application metadata, constants, and service endpoints: [`Pianoscribe/pianoscribe/core/config.py`](https://github.com/Justagwas/Pianoscribe/blob/main/Pianoscribe/pianoscribe/core/config.py)
- Runtime setting serialization and normalization: [`Pianoscribe/pianoscribe/core/config_service.py`](https://github.com/Justagwas/Pianoscribe/blob/main/Pianoscribe/pianoscribe/core/config_service.py)
- Runtime and path resolution: [`Pianoscribe/pianoscribe/core/paths.py`](https://github.com/Justagwas/Pianoscribe/blob/main/Pianoscribe/pianoscribe/core/paths.py)
- Model acquisition, storage, and validation: [`Pianoscribe/pianoscribe/core/model_service.py`](https://github.com/Justagwas/Pianoscribe/blob/main/Pianoscribe/pianoscribe/core/model_service.py)
- GPU runtime pack management: [`Pianoscribe/pianoscribe/core/runtime_pack_service.py`](https://github.com/Justagwas/Pianoscribe/blob/main/Pianoscribe/pianoscribe/core/runtime_pack_service.py)
- Audio analysis and event decoding: [`Pianoscribe/pianoscribe/core/piano_engine.py`](https://github.com/Justagwas/Pianoscribe/blob/main/Pianoscribe/pianoscribe/core/piano_engine.py)
- MIDI construction and output naming: [`Pianoscribe/pianoscribe/core/conversion_service.py`](https://github.com/Justagwas/Pianoscribe/blob/main/Pianoscribe/pianoscribe/core/conversion_service.py)

</details>

## Security and OS Warnings

- Windows SmartScreen may display a warning for a new or unsigned release.
- Obtain Pianoscribe only from the official distribution locations:
  - <https://github.com/Justagwas/Pianoscribe/releases>
  - <https://www.justagwas.com/projects/pianoscribe/download/>
  - <https://sourceforge.net/projects/pianoscribe/>
- Refer to the repository [Security Policy](https://github.com/Justagwas/Pianoscribe/security/policy) for private vulnerability reporting.

## Contributing

Contributions are welcome.

- Start with [`.github/CONTRIBUTING.md`](https://github.com/Justagwas/Pianoscribe/blob/main/.github/CONTRIBUTING.md)
- Follow the shared [Code of Conduct](https://github.com/Justagwas/.github/blob/main/CODE_OF_CONDUCT.md)
- Use [Issues](https://github.com/Justagwas/Pianoscribe/issues) for defect reports, feature proposals, and questions
- Wiki: <https://github.com/Justagwas/Pianoscribe/wiki>

## Contact

- Email: [email@justagwas.com](mailto:email@justagwas.com)
- Website: <https://www.justagwas.com/projects/pianoscribe/>

## License

Licensed under the GNU General Public License v3.0 (GPL-3.0).

See [`LICENSE`](https://github.com/Justagwas/Pianoscribe/blob/main/LICENSE).
