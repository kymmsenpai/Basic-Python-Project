import random
import colorama
from colorama import Fore, Back, Style
import time

colorama.init(autoreset=True)

# Show title game
border = Fore.BLUE + '==================================================================================================='
title = Fore.GREEN + ''' _   _                             _           _                       _    _    _       _    _   
| | | |__._ _  ___  _ _ _   _ _ _ | |_  ___  _| |_   _ _  ___  _ _   _| |_ | |_ <_>._ _ | |__| |__
| | | / /| ' |/ . \| | | | | | | || . |<_> |  | |   | | |/ . \| | |   | |  | . || || ' || / /| / /
|_| |_\_\|_|_|\___/|__/_/  |__/_/ |_|_|<___|  |_|   `_. |\___/`___|   |_|  |_|_||_||_|_||_\_\|_\_\ 
                                                    <___'                                         '''
print(border)
print(title.center(len(border)))
print(border)

# show number with use randint, then get user input where there is user number or not
def getshow_number(selection):
  temp =[]
  i = 0
  while i < 6:
    x = random.randint(1,10)
    if x not in temp:
      temp.append(x)
      i+=1
  print(Fore.RED + f'''
  {temp[0]}  {temp[1]}  {temp[2]} 
  {temp[3]}  {temp[4]}  {temp[5]} 
  ''')
  get = input(Fore.GREEN + 'Is there your number (y/n) : ')
  print('')
  print(border)
  if get.lower() == 'y':
    for key,value in selection.items():
      if key in temp:
        value.append(True)
      else:
        value.append('-')
  else:
    for key,value in selection.items():
      if key in temp:
        value.append(False)
      else:
        value.append('-')

# show computer's order for user to think one number between 1 - 10
def caution():
  print('')
  print(Fore.RED + '[!] Think of a number 1 - 10, the computer will guess the number you think')
  print('')
  print(border)
  time.sleep(2) 

# offer user if they want to play again
def ask_again():
  print('')
  user = input(Fore.RED + '[?] do you want to play again ? (y/n) : ')
  print('')
  print(border)
  if user.lower() == 'y':
    caution() # show output where user should think one number between 1 - 10
    play()
  else:
    exit_game()

# give last message to user when user want to exit 
def exit_game():
  print('')
  print(Fore.GREEN + 'THANKYOU FOR PLAYING THIS GAME'.center(len(border)))
  print('')
  print(border)
  exit()

# after output title computer give menu to user where they want play or not
print(Fore.GREEN + '''
[1] Play
[2] Exit
''')
ask = int(input(Fore.GREEN + 'Select using numbers => '))
print('')
print(border)

# computer will guess your number with use dictionary and while
def play():
  selection = {
  1 : [],
  2 : [],
  3 : [],
  4 : [],
  5 : [],
  6 : [],
  7 : [],
  8 : [],
  9 : [],
  10 : [],
  }
  if ask == 1:
    last = ['x','x'] # contains the number the user thinks of
    while len(last) != 1: # if variable last have more than 1 value, computer will ask user until variable last have one value
      last = [] 
      getshow_number(selection) # show number and get information if there is number's user or not
      for key,value in selection.items():
        if False not in value: # if value number in dictionary not containing false, therefore thats number become last's variable value
          last.append(key)
        if len(value) == 10:
          play()
    print('')
    print(Fore.GREEN + f'Your number is {Fore.RED + str(last[0])}'.center(len(border))) # show user number
    print('')
    print(border)
    ask_again() # give offer to user which is user want to play again or not
  else:
    exit_game()

caution() # show output where user should think one number between 1 - 10
# first play
play()