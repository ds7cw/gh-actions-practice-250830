import requests
from bs4 import BeautifulSoup
import re

# Replace with your target playlist URL
playlist_url = "https://www.youtube.com/playlist?list=PLAAE66433681598F2"

# Headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Safari/537.36"
}

# Send GET request
response = requests.get(playlist_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find all video title anchors
video_links = soup.find_all("a", id="video-title")

# Extract artist and song title
for link in video_links:
    title = link.get("title") or link.text.strip()
    if title:
        # Basic split assuming format "Artist - Song Title"
        parts = re.split(r"\s*-\s*", title, maxsplit=1)
        if len(parts) == 2:
            artist, song = parts
        else:
            artist, song = "Unknown", title
        print(f"Artist: {artist.strip()} | Song: {song.strip()}")
