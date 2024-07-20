# m4a_to_wav
Convert m4a file to wav file in python
# M4A to WAV Converter

This Python script converts all `.m4a` files in a specified directory to `.wav` format using FFmpeg.

## Requirements

- Python 3.x
- pydub: Install the pydub library. You can run  pip install pydub in terminal.
- FFmpeg

## Installation

1. **Download and Install FFmpeg:**
   - Go to the [FFmpeg download page](https://ffmpeg.org/download.html).
   - Download the version appropriate for your operating system.
   - Extract the downloaded archive.
   - Create folder in c drive. Name as ffmpeg.Then copy the content of bin of extracted folder to ffmpeg folder of c drive.
   - Give the path name of ffmpeg in environment (e.g., `C:\ffmpeg`)
   - create one folder to store all .m4a files.
   - create another folder for storing the .wav files
   

2. **Clone this Repository:**
   ```bash
   git clone https://github.com/yourusername/m4a-to-wav-converter.git
   cd m4a-to-wav-converter
