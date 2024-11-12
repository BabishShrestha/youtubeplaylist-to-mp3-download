import os
import requests
import re
import subprocess

# Helper functions
def foldertitle(url):
    try:
        res = requests.get(url)
    except Exception as e:
        print(f'No internet or error: {e}')
        return False

    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]
    else:
        print('Incorrect attempt.')
        return False

    return cPL

def link_snatcher(url):
    our_links = []
    try:
        res = requests.get(url)
    except Exception as e:
        print(f'No internet or error: {e}')
        return False

    plain_text = res.text

    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]
    else:
        print('Incorrect Playlist.')
        return False

    tmp_mat = re.compile(r'watch\?v=\S+?list=' + cPL)
    mat = re.findall(tmp_mat, plain_text)

    for m in mat:
        work_m = 'https://youtube.com/' + m
        if work_m not in our_links:
            our_links.append(work_m)

    return our_links

BASE_DIR = os.getcwd()
print('WELCOME TO PLAYLIST DOWNLOADER - MP3 VERSION USING yt-dlp')

url = input("\nSpecify your playlist URL: ")

our_links = link_snatcher(url)
if not our_links:
    print("No links found, exiting...")
    exit()

os.chdir(BASE_DIR)
new_folder_name = foldertitle(url)
if not new_folder_name:
    print("Error retrieving folder title, exiting...")
    exit()

# Create folder for downloads
try:
    os.mkdir(new_folder_name[:7])
except FileExistsError:
    print('Folder already exists')

os.chdir(new_folder_name[:7])
SAVEPATH = os.getcwd()
print(f'\nFiles will be saved to {SAVEPATH}\n')

print('Connecting...\n')

# Use yt-dlp to download audio for all links
for link in our_links:
    try:
        print(f'Downloading audio for: {link}')
        command = f'yt-dlp -x --audio-format mp3 -o "{SAVEPATH}/%(title)s.%(ext)s" {link}'
        subprocess.run(command, shell=True)
        print('Audio Downloaded and Converted to MP3')
    except Exception as e:
        print(f'Error downloading {link}: {e}')

print('Downloading finished')
print(f'\nAll your MP3 files are saved at --> {SAVEPATH}')
