# A2M - Audio to MIDI

<div align="center">

[![Code: GitHub](https://img.shields.io/badge/Code-GitHub-111827.svg?style=flat&logo=github&logoColor=white)](https://github.com/Justagwas/A2M)
[![Website](https://img.shields.io/badge/Website-A2M-0ea5e9.svg?style=flat&logo=google-chrome&logoColor=white)](https://Justagwas.com/projects/a2m)
[![Mirror: SourceForge](https://img.shields.io/badge/Mirror-SourceForge-ff6600.svg?style=flat&logo=sourceforge&logoColor=white)](https://sourceforge.net/projects/a2m/)

</div>

<p align="center">
  <img
    width="128"
    height="128"
    alt="A2M Logo"
    src="https://github.com/user-attachments/assets/64a4aa9f-e130-4eb7-9f29-77fc449567f6"
  />
</p>

<div align="center">

[![Download (Windows)](https://img.shields.io/badge/Download-Windows%20(A2MSetup.exe)-2563eb.svg?style=flat&logo=windows&logoColor=white)](https://github.com/Justagwas/A2M/releases/latest/download/A2MSetup.exe)

</div>

<p align="center"><b>Turn piano recordings into accurate, editable MIDI</b></p>

<p align="center">Private local transcription with adjustable performance settings and optional graphics card acceleration</p>

<div align="center">

[![Version](https://img.shields.io/github/v/tag/Justagwas/A2M.svg?label=Version)](https://github.com/Justagwas/A2M/tags)
[![License](https://img.shields.io/github/license/Justagwas/A2M.svg)](https://github.com/Justagwas/A2M/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Justagwas/A2M/main.svg?style=flat&cacheSeconds=3600)](https://github.com/Justagwas/A2M/commits/main)
[![Open Issues](https://img.shields.io/github/issues/Justagwas/A2M.svg)](https://github.com/Justagwas/A2M/issues)
[![Stars](https://img.shields.io/github/stars/Justagwas/A2M.svg?style=flat&cacheSeconds=3600)](https://github.com/Justagwas/A2M/stargazers)
![Downloads (7d)](https://img.shields.io/badge/dynamic/json?style=flat&url=https%3A%2F%2Fdownload-stats-worker.justagwas.workers.dev%2Fdownloads%2Fa2m%3Frange%3Dweek&query=%24.data.weekly.all&label=Downloads%20(7d))

</div>

## Overview

A2M is a Windows application that listens to a piano recording and turns the performance into a MIDI file you can open, edit, and arrange. It identifies the notes, their timing and dynamics, and optional pedal use without uploading the recording for analysis.

Clean solo piano recordings provide the clearest results. You can also decide how much of the computer A2M should use, allowing it to work quietly in the background or finish more quickly when resources are available.

## Basic usage

1. Download and install from the [latest release](https://github.com/Justagwas/A2M/releases/latest/download/A2MSetup.exe).
2. Launch A2M and allow the initial transcription package to download when prompted.
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

## How A2M turns a recording into MIDI

A2M works from the sound of the performance itself. It listens in short overlapping sections so that notes near a boundary still retain their musical context.

Several complementary views of the sound help separate quiet notes, strong attacks, and overlapping harmonies. A2M then chooses the most consistent sequence of notes and pedals, refines their timing and dynamics, and brings every section back together on one continuous timeline.

The completed performance is saved as an editable MIDI file. Existing transcriptions are not overwritten unintentionally.

For a visual explanation, worked results, and the full technical account, visit the [A2M Wiki](https://github.com/Justagwas/A2M/wiki).

## Project resources

- Project page: <https://www.justagwas.com/projects/a2m>
- Download page: <https://www.justagwas.com/projects/a2m/download>
- Documentation: <https://github.com/Justagwas/A2M/wiki>
- Releases: <https://github.com/Justagwas/A2M/releases>

<details>
<summary>For Developers</summary>

### Requirements

- Windows (primary runtime target).
- Python 3.11 or later.
- Dependencies in [`A2M/requirements.txt`](https://github.com/Justagwas/A2M/blob/main/A2M/requirements.txt).

### Running From Source

```powershell
cd A2M
py -m pip install -r requirements.txt
py A2M.py
```

### Configuration Files

- Application metadata, constants, and service endpoints: [`A2M/a2m/core/config.py`](https://github.com/Justagwas/A2M/blob/main/A2M/a2m/core/config.py)
- Runtime setting serialization and normalization: [`A2M/a2m/core/config_service.py`](https://github.com/Justagwas/A2M/blob/main/A2M/a2m/core/config_service.py)
- Runtime and path resolution: [`A2M/a2m/core/paths.py`](https://github.com/Justagwas/A2M/blob/main/A2M/a2m/core/paths.py)
- Model acquisition, storage, and validation: [`A2M/a2m/core/model_service.py`](https://github.com/Justagwas/A2M/blob/main/A2M/a2m/core/model_service.py)
- GPU runtime pack management: [`A2M/a2m/core/runtime_pack_service.py`](https://github.com/Justagwas/A2M/blob/main/A2M/a2m/core/runtime_pack_service.py)
- Audio analysis and event decoding: [`A2M/a2m/core/piano_engine.py`](https://github.com/Justagwas/A2M/blob/main/A2M/a2m/core/piano_engine.py)
- MIDI construction and output naming: [`A2M/a2m/core/conversion_service.py`](https://github.com/Justagwas/A2M/blob/main/A2M/a2m/core/conversion_service.py)

</details>

## Security and OS Warnings

- Windows SmartScreen may display a warning for a new or unsigned release.
- Obtain A2M only from the official distribution locations:
  - <https://github.com/Justagwas/A2M/releases>
  - <https://www.justagwas.com/projects/a2m/download>
  - <https://sourceforge.net/projects/a2m/>
- Refer to [`.github/SECURITY.md`](https://github.com/Justagwas/A2M/blob/main/.github/SECURITY.md) for the security policy and private vulnerability reporting procedure.

## Contributing

Contributions are welcome.

- Start with [`.github/CONTRIBUTING.md`](https://github.com/Justagwas/A2M/blob/main/.github/CONTRIBUTING.md)
- Follow [`.github/CODE_OF_CONDUCT.md`](https://github.com/Justagwas/A2M/blob/main/.github/CODE_OF_CONDUCT.md)
- Use [Issues](https://github.com/Justagwas/A2M/issues) for defect reports, feature proposals, and questions
- Wiki: <https://github.com/Justagwas/A2M/wiki>

## Contact

- Email: [email@justagwas.com](mailto:email@justagwas.com)
- Website: <https://www.justagwas.com/projects/a2m>

## License

Licensed under the GNU General Public License v3.0 (GPL-3.0).

See [`LICENSE`](https://github.com/Justagwas/A2M/blob/main/LICENSE).
