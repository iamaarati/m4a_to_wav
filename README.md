# m4a_to_wav using ffmpeg (Media Transcoding)
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

      ![image](https://github.com/user-attachments/assets/0b797067-093f-4020-b4e4-ef4532f22aa9)
   - Give the path name of ffmpeg in environment (e.g., `C:\ffmpeg`)

      ![image](https://github.com/user-attachments/assets/4f1a2f52-0325-4db5-897c-f1e0b2618363)
     
     ![image](https://github.com/user-attachments/assets/e2afd18b-8819-4e8b-a5f6-8c6acb44bdde)
   - create one folder to store all .m4a files.
   - create another folder for storing the .wav files
     ![image](https://github.com/user-attachments/assets/6b9a2ef2-83d3-45cb-bec2-d9a84f6b3c14)

   

2. **Clone this Repository:**
   ```bash
   git clone https://github.com/yourusername/m4a-to-wav-converter.git
   cd m4a-to-wav-converter
