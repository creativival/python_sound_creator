# Python Sound Creator

A simple Python project to generate short sound effects (SE) like beeps, door knocks, success/fail jingles, etc., and export them as MP3 files. The project demonstrates basic techniques for synthesizing waveforms (sine waves, white noise, etc.) and processing them using pydub.

## Features

- Generate simple sine wave tones (beeps).
- Create short white noise bursts (e.g., door knock).
- Combine tones to form basic jingles (e.g., success or fail sound effects).
- Export the generated audio as MP3 files.

## Requirements

- Python 3.7 or later
- pydub (for audio handling and format conversion)
- ffmpeg (required by pydub for MP3 export)
- (Optional) Any virtual environment or package manager you prefer, such as venv or conda.

### Installation

1. Clone this repository (or download the project files):

```bash
git clone https://github.com/<your-username>/python_sound_creator.git
cd python_sound_creator
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt or
```

or

```bash
pip install pydub 
```

3. Make sure ffmpeg is installed and added to your PATH.

- On macOS: brew install ffmpeg
- On Linux (Ubuntu/Debian): sudo apt-get install ffmpeg
- On Windows: Download from the official site or Windows builds, then add it to your system PATH.

## Usage

1. Generate and export sound effects

In the main script (adjust the file name/path as needed), you will see
functions to generate different types of sounds:

- Simple beep
- Door knock
- Success jingle
- Fail jingle

Each function uses either a sine wave generator or white noise generator, possibly with a fade in/out effect or pitch changes.

To run the script:

```bash
python sound_creator.py
```

After running, you should find MP3 files (e.g., beep.mp3, door_knock.mp3, success.mp3, fail.mp3) in the same directory.

## License

This project is released under the `Unlicense`.

You are free to use, modify, and redistribute this software `without any
restrictions`.

```
This is free and unencumbered software released into the public
domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
```
