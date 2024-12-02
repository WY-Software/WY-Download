import yt_dlp as youtube_dl

async def download(uid: int, link: str) -> None:
    ydl = youtube_dl.YoutubeDL({'outtmpl': f'{uid}.%(ext)s'})

    ydl.download([link])
