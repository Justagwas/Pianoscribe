# Pianoscribe

<div align="center">

[![Code: GitHub](https://img.shields.io/badge/Code-GitHub-111827.svg?style=flat&logo=github&logoColor=white)](https://github.com/Justagwas/Pianoscribe)
[![Website](https://img.shields.io/badge/Website-Pianoscribe-0ea5e9.svg?style=flat&logo=google-chrome&logoColor=white)](https://Justagwas.com/projects/pianoscribe)
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

<p align="center"><b>Turn piano recordings into accurate, editable MIDI</b></p>

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

Pianoscribe is a Windows application that listens to a piano recording and turns the performance into a MIDI file you can open, edit, and arrange. It identifies the notes, their timing and dynamics, and optional pedal use without uploading the recording for analysis.

Clean solo piano recordings provide the clearest results. You can also decide how much of the computer Pianoscribe should use, allowing it to work quietly in the background or finish more quickly when resources are available.

## Basic usage

1. Download and install from the [latest release](https://github.com/Justagwas/Pianoscribe/releases/latest/download/PianoscribeSetup.exe).
2. Launch Pianoscribe and allow the initial transcription package to download when prompted.
3. Select **Choose Audio** and open a piano recording.
4. Choose whether the result should include natural dynamics and pedal information.
5. Optionally adjust performance settings to suit the computer.
6. Click **Convert to MIDI**.
7. Open the finished MIDI from the output folder.

## Features

- Accurate transcription designed for clear solo piano recordings.
- Private processing with no source recording upload.
- Support for MP3, WAV, FLAC, OGG, M4A, AAC, WMA, AIFF, and AIF files when the required codec is available.
- Note timing, dynamics, sustain, and soft pedal recognition.
- Expressive or even note strength, depending on the intended result.
- Adjustable CPU use and graphics memory limits.
- Optional CUDA or DirectML acceleration on supported hardware.
- Configurable save location, interface size, and update checks.
- Safe cancellation during setup, downloads, and transcription.

## How Pianoscribe turns a recording into MIDI

Pianoscribe works from the sound of the performance itself. It listens in short overlapping sections so that notes near a boundary still retain their musical context.

Several complementary views of the sound help separate quiet notes, strong attacks, and overlapping harmonies. Pianoscribe then chooses the most consistent sequence of notes and pedals, refines their timing and dynamics, and brings every section back together on one continuous timeline.

The completed performance is saved as an editable MIDI file. Existing transcriptions are not overwritten unintentionally.

For a visual explanation, worked results, and the full technical account, visit the [Pianoscribe Wiki](https://github.com/Justagwas/Pianoscribe/wiki).

## Project resources

- Project page: <https://www.justagwas.com/projects/pianoscribe>
- Download page: <https://www.justagwas.com/projects/pianoscribe/download>
- Documentation: <https://github.com/Justagwas/Pianoscribe/wiki>
- Releases: <https://github.com/Justagwas/Pianoscribe/releases>

<details>
<summary>For Developers</summary>

### Requirements

- Windows (primary runtime target).
- Python 3.11 or later.
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
  - <https://www.justagwas.com/projects/pianoscribe/download>
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
- Website: <https://www.justagwas.com/projects/pianoscribe>

## License

Licensed under the GNU General Public License v3.0 (GPL-3.0).

See [`LICENSE`](https://github.com/Justagwas/Pianoscribe/blob/main/LICENSE).
