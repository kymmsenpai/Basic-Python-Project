from pytube import YouTube

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f'{percentage_of_completion} %', end='\r')

url = "https://www.youtube.com/watch?v=xVdAtjO696Y"

# Create the YouTube object first
yt_obj = YouTube(url)

# Then register the callback
yt_obj.register_on_progress_callback(on_progress)

# Download the video, getting back the file path the video was downloaded to
file_path = yt_obj.streams.filter(progressive=True).get_highest_resolution().download()
print(f"file_path is {file_path}")

# ui = '|\/|/\|/\|'
#     for i in range(len(ui)):
#         print(f'{ui[i]} {percentage_of_completion}% Progress', end='\r')
#         time.sleep(0.2)