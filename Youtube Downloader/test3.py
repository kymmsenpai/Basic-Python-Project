from pytube import YouTube
from tqdm import tqdm

video_url = "https://www.youtube.com/watch?v=kEC2AHQg0Qo"
yt = YouTube(video_url)


streams = yt.streams.filter(progressive=True)
stream = streams.get_highest_resolution()


file_size = stream.filesize
progress_bar = tqdm(total=file_size, unit='bytes', unit_scale=True)

def progress_callback(chunk, file_handle, bytes_remaining):
    progress_bar.update(file_size - bytes_remaining)

yt.register_on_progress_callback(progress_callback)

stream.download()
progress_bar.close()


