import yt_dlp

yt_dlp.YoutubeDL({'format': 'best', 'outtmpl': '%(title)s.%(ext)s'}).download(['https://youtube.com/shorts/BIprWT22_bE?si=AtTYBzHs8gLKEr_b'])