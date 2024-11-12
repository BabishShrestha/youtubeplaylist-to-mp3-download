# YouTube Playlist Downloader

A simple tool to download audio from a YouTube playlist.

## Prerequisites

Make sure you have the following installed:

1. **Python** (version 3.6 or higher)
2. **FFmpeg**: Required for converting video to audio. Installation instructions are provided below.

## Installation

### Step 1: Install Dependencies

Run the following command to install the necessary Python packages:

```bash
pip install pytube requests pydub
```
### Step 2: Install FFmpeg

FFmpeg is needed for handling media formats. Follow these steps to install FFmpeg:

- Visit the [FFmpeg installation guide](https://phoenixnap.com/kb/ffmpeg-windows) and follow the instructions for your operating system.

### Step 3: Run the Script

1. Clone or download this repository.
2. Run the script and input your YouTube playlist URL when prompted:

```bash
python your_script_name.py
```
## Usage

1. Execute the script using Python by running the following command in your terminal:

    ```bash
    python your_script_name.py
    ```

2. You will be prompted to enter the URL of the YouTube playlist you want to download.

3. The script will automatically start downloading and converting the audio files from the playlist.

4. Once the process is complete, the audio files will be saved in your working directory.

---

## Notes

- **FFmpeg**: Ensure that FFmpeg is properly installed and added to your system's `PATH`. This is necessary for audio conversion.
  
- **Dependencies**: If you encounter issues related to missing dependencies, make sure that you've installed the required Python packages using:

    ```bash
    pip install pytube requests pydub
    ```

- **YouTube Playlist Limitations**: Be mindful that downloading entire playlists may be subject to YouTube's terms of service. Use this tool responsibly.

- **Troubleshooting**: If you run into errors, refer to the documentation for the libraries used:
  - [Pytube documentation](https://pytube.io/)
  - [Pydub documentation](https://pydub.com/)

- **Output**: The downloaded audio files will be saved in the same directory as the script unless specified otherwise.

---

## Enjoy!

Happy downloading and enjoy your audio!
