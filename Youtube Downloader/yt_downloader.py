from pytube import YouTube
import time
from colorama import Fore, Back, Style
import colorama
from tqdm import tqdm    

def downloadVideo():
  colorama.init(autoreset=True)

  border = f'{Fore.LIGHTRED_EX}----------------------------------------------------------------------------------------'

  # app view
  print(f'''{Fore.LIGHTYELLOW_EX}
  ██─██─████─█─█─███─█─█─████──███────████──████─█───█─█──█─█───████─████─████──███─████
  ─███──█──█─█─█──█──█─█─█──██─█──────█──██─█──█─█───█─██─█─█───█──█─█──█─█──██─█───█──█
  ──█───█──█─█─█──█──█─█─████──███────█──██─█──█─█─█─█─█─██─█───█──█─████─█──██─███─████
  ──█───█──█─█─█──█──█─█─█──██─█──────█──██─█──█─█████─█──█─█───█──█─█──█─█──██─█───█─█─
  ──█───████─███──█──███─████──███────████──████──█─█──█──█─███─████─█──█─████──███─█─█─
  ''')
  print(border)
  print(f'{Fore.LIGHTBLUE_EX}{time.ctime()}')
  print(border)

  # user input link and place
  link  = input(f'{Fore.YELLOW}link      : ') 
  place = input(f'{Fore.YELLOW}direktori (example = D:/Videos): ') 
  print(border)

  # get video from link
  yt = YouTube(link)

  # show information contained in the video
  print(f'{Fore.GREEN}Title  : {yt.title}')
  print(f'{Fore.GREEN}Views  : {yt.views}')
  print(f'{Fore.GREEN}Author : {yt.author}')
  print(border)

  streams = yt.streams.filter(progressive=True)
  stream = streams.get_highest_resolution()

  file_size = stream.filesize
  progress_bar = tqdm(total=file_size, unit='bytes', unit_scale=True, ncols=(len(border)-5))

  def progress_callback(chunk, file_handle, bytes_remaining):
    size = file_size - bytes_remaining
    progress_bar.update(size - progress_bar.n)

  yt.register_on_progress_callback(progress_callback)

  stream.download(place)
  progress_bar.close()
  # # get highest resolution and donwload it
  # streams = yt.streams.filter(progressive=True)
  # stream = streams.get_highest_resolution()
  # file_size = stream.filesize

  # progress_bar = tqdm(total=file_size, unit=bytes, unit_scale=True)


  # def on_progress(stream, chunk, bytes_remaining):
  #   # total_size = stream.filesize
  #   # bytes_downloaded = total_size - bytes_remaining
  #   # percentage_of_completion = int(bytes_downloaded / total_size * 100)
  #   progress_bar.update(file_size - bytes_remaining)
  
  # # on progress
  # yt.register_on_progress_callback(on_progress)

  # stream.download(place)

  # # show if your downloading is done
  print(f'{Fore.LIGHTBLUE_EX}DONE!!!')
  print(border)

if __name__ == '__main__':
  downloadVideo()
