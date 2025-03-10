# VLC Player Clone

A simple **VLC Player Clone** built using **Python, PyQt5, and VLC**, with support for local file playback, URL streaming (including **YouTube videos**), PiP mode, and more.

## 🚀 Features
- 🎬 **Play Local Files**: Open and play any media file.
- 🌍 **Stream Online URLs**: Play videos from direct URLs.
- 🎥 **YouTube Streaming**: Paste a YouTube URL, and it plays automatically.
- 🔊 **Adjust Volume**: Control audio levels with a slider.
- ⏩ **Playback Speed**: Change speed from 0.5x to 2.0x.
- 🖥 **Picture-in-Picture Mode**: Toggle fullscreen mode.
- ⏳ **Sleep Timer**: Auto-stop playback after a set time.
- 🏷 **Metadata Display**: Show media title, artist, and duration.

---

## 🛠 Installation
### 1️⃣ Install Dependencies
Make sure you have **Python 3.7+** installed, then run:
```bash
pip install pyqt5 python-vlc yt-dlp
```

### 2️⃣ Install VLC Media Player
- **Windows:** [Download VLC](https://www.videolan.org/vlc/)
- **Linux/macOS:** Install via package manager

Make sure VLC is added to your system's PATH.

---

## ▶️ How to Use
### 🎬 **Playing Local Files**
1. Click **"Open File"**.
2. Select a media file (`.mp4`, `.avi`, `.mkv`, etc.).
3. The video starts playing.

### 🌍 **Streaming Online Videos**
1. Paste the **video URL** in the text box.
2. Click **"Stream URL"**.
3. If it's a **YouTube video**, the script will fetch the direct URL and play it.

### 📺 **Enabling PiP Mode**
- Click **"PiP Mode"** to toggle fullscreen.

### 🎵 **Adjusting Playback**
- **Volume Slider**: Change audio level.
- **Playback Speed**: Adjust from **0.5x to 2.0x**.

### 💤 **Sleep Timer**
- Check **"Enable Sleep Timer"** to auto-stop playback.

---

## 🛠 Troubleshooting
### 🔴 "VLC Not Found" Error
- Ensure **VLC is installed and added to PATH**.

### 🔴 "YouTube Video Not Playing"
- **Install/Update `yt-dlp`**:
  ```bash
  pip install --upgrade yt-dlp
  ```
- Some YouTube videos may have **restrictions** that prevent streaming.

---

### 🚀 Enjoy your VLC Clone! 🎥🔥

