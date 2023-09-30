from pytube import YouTube
from sys import argv
import time
from colorama import Fore, Back, Style
import colorama

border = Fore.LIGHTRED_EX + '--------------------------------------------------'

colorama.init(autoreset=True)

# get video from link
link = argv[1]
yt = YouTube(link)

# app view
print('''
______██████████████
-____██▓▓▓▓▓▓▓▓▓ M ▓████
-__██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
-__██████░░░░██░░██████
██░░░░████░░██░░░░░░░░██
██░░░░████░░░░██░░░░░░██
-__████░░░░░░██████████
-__██░░░░░░░░░░░░░██
_____██░░░░░░░░░██
-______██░░░░░░██
-____██▓▓████▓▓▓█
-_██▓▓▓▓▓▓████▓▓█
██▓▓▓▓▓▓███░░███░
-__██░░░░░░███████
-____██░░░░███████
-______██████████
-_____██▓▓▓▓▓▓▓▓▓██
-_____█████████████
''')
print(border)
print(Fore.LIGHTBLUE_EX,time.ctime())
print(border)

# show information contained in the video
print('Title  : ', yt.title)
print('Views  : ', yt.views)
print('Author : ',yt.author)

# get highest resolution and donwload it
yt_dwnld = yt.streams.get_highest_resolution()
yt_dwnld.download('D:/Video')