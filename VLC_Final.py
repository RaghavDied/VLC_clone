
import sys
import vlc
import os
import yt_dlp
os.environ["QT_MULTIMEDIA_PREFERRED_PLUGINS"] = "windowsmediafoundation"
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QSlider, QLabel, QLineEdit, QHBoxLayout, QCheckBox, QFrame
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QGridLayout

class VLCClone(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VLC Player Clone")
        self.setGeometry(100, 100, 1000, 700)

        # VLC Instance
        self.instance = vlc.Instance()
        self.media_player = self.instance.media_player_new()

        # Video Frame
        self.video_frame = QFrame(self)
        self.video_frame.setStyleSheet("background-color: black;")
        self.video_frame.setFixedHeight(400)  # Increased height
        
        if sys.platform.startswith("linux"):
            self.media_player.set_xwindow(self.video_frame.winId())
        else:
            self.media_player.set_hwnd(self.video_frame.winId())
        
        # UI Elements
        self.open_btn = QPushButton("Open File")
        self.open_btn.clicked.connect(self.open_file)

        self.stream_btn = QPushButton("Stream URL")
        self.stream_btn.clicked.connect(self.stream_url)

        self.play_btn = QPushButton("Play")
        self.play_btn.clicked.connect(self.media_player.play)

        self.pause_btn = QPushButton("Pause")
        self.pause_btn.clicked.connect(self.media_player.pause)

        self.stop_btn = QPushButton("Stop")
        self.stop_btn.clicked.connect(self.media_player.stop)
        
        self.pip_btn = QPushButton("PiP Mode")
        self.pip_btn.clicked.connect(self.toggle_pip)

        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(50)
        self.volume_slider.valueChanged.connect(self.change_volume)

        self.playback_slider = QSlider(Qt.Horizontal)
        self.playback_slider.setMinimum(50)
        self.playback_slider.setMaximum(200)
        self.playback_slider.setValue(100)
        self.playback_slider.valueChanged.connect(self.change_playback_speed)
        
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter stream URL...")

        self.metadata_label = QLabel("Metadata: None")

        self.sleep_timer_checkbox = QCheckBox("Enable Sleep Timer")
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.video_frame)
        
        layout.addWidget(self.url_input)

        btn_layout = QGridLayout()
        btn_layout.addWidget(self.open_btn, 0, 0, 1, 2)  # Stretch Open & Stream Buttons
        btn_layout.addWidget(self.stream_btn, 0, 2, 1, 2)
        btn_layout.addWidget(self.play_btn, 1, 0)
        btn_layout.addWidget(self.pause_btn, 1, 1)
        btn_layout.addWidget(self.stop_btn, 1, 2)
        btn_layout.addWidget(self.pip_btn, 1, 3)
        layout.addLayout(btn_layout)
        
        layout.addWidget(QLabel("Volume"))
        layout.addWidget(self.volume_slider)
        
        layout.addWidget(QLabel("Playback Speed"))
        layout.addWidget(self.playback_slider)
        
        layout.addWidget(self.sleep_timer_checkbox)
        layout.addWidget(self.metadata_label)
        
        self.setLayout(layout)

        # Timer to update metadata
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_metadata)
        self.timer.start(2000)  # Every 2 seconds

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Video", "", "Media Files (*.mp4 *.avi *.mkv *.mp3 *.wav)")
        if file_path:
            media = self.instance.media_new(file_path)
            self.media_player.set_media(media)
            
            # Subtitles Support (Auto-load SRT)
            subtitle_path = file_path.rsplit(".", 1)[0] + ".srt"
            self.media_player.video_set_subtitle_file(subtitle_path)

            self.media_player.set_hwnd(self.video_frame.winId())
            self.media_player.play()

    def stream_url(self):
        url = self.url_input.text()
        if "youtube.com" in url or "youtu.be" in url:
            with yt_dlp.YoutubeDL({'format': 'best'}) as ydl:
                info = ydl.extract_info(url, download=False)
                url = info['url']
        
        if url:
            media = self.instance.media_new(url)
            self.media_player.set_media(media)
            self.media_player.set_hwnd(self.video_frame.winId())
            self.media_player.play()

    def change_volume(self, value):
        self.media_player.audio_set_volume(value)

    def change_playback_speed(self, value):
        self.media_player.set_rate(value / 100.0)

    def update_metadata(self):
        media = self.media_player.get_media()
        if media:
            media.parse()
            title = media.get_meta(vlc.Meta.Title) or "Unknown Title"
            artist = media.get_meta(vlc.Meta.Artist) or "Unknown Artist"
            duration = media.get_duration() // 1000  # Convert ms to seconds
            self.metadata_label.setText(f"Title: {title}, Artist: {artist}, Duration: {duration} sec")
    
    def toggle_pip(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VLCClone()
    player.show()
    sys.exit(app.exec_())