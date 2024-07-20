import subprocess
import os

input_directory = r"C:\Users\aarat\Downloads\datasets_collected"
output_directory = r"C:\Users\aarat\Downloads\wav_files"
ffmpeg_path = r"C:\ffmpeg\ffmpeg.exe"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for dirpath, dirnames, filenames in os.walk(input_directory):
    for filename in filenames:
        if filename.endswith('.m4a'):
            m4a_path = os.path.join(dirpath, filename)
            wav_filename = filename.replace('.m4a', '.wav')
            wav_path = os.path.join(output_directory, wav_filename)
            command = [ffmpeg_path, '-i', m4a_path, wav_path]
            try:
                result = subprocess.run(command, capture_output=True, text=True, check=True)
                print(f"Converted {filename} to WAV.")
            except subprocess.CalledProcessError as e:
                print(f"Conversion failed for {filename}: {e.stderr}")
            except FileNotFoundError as e:
                print(f"File not found: {e}")
            except PermissionError as e:
                print(f"Permission error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
