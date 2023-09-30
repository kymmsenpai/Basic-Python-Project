import turtle
import keyboard
import time

# color
clr1 = ['#358f80','#d00000']
clr2 = ['#469d89','#dc2f02']
clr3 = ['#56ab91','#e85d04']
clr4 = ['#67b99a','#f48c06']

def nyala():
  # background
  s = turtle.Screen()
  s.bgcolor('#fefae0')
  flower(100,clr1)
  flower(80,clr2)
  flower(60,clr3)
  flower(40,clr4)
  letter(ask)

# satu bunga
def flower(size,color):
  t = turtle.Turtle()
  t.speed(100)
  for side in range(10):
    for half in range(2):
      t.color(color[half])
      t.begin_fill()
      t.pensize(2)
      t.circle(size,90)
      t.lt(90)
      t.end_fill()  
    t.lt(36)
  t.ht()

def letter(name):
  word = turtle.Turtle()
  word.color('#67b69a')
  word.ht()
  word.penup()
  word.goto(0,-200)
  word.pendown()
  word.write(f'Semangat yaaa {name}',align='center',font=('Arial',20,'bold'))

def enterr():
  print('Teken spasi dong biar bunganya muncul')
  turtle.onkeypress(nyala,'space')
  turtle.listen()
  turtle.mainloop()

# tanya
ask = input('Namanya siapa nih!? : ')
while ask.isalpha() == False:
  ask = input('Isi yang bener namanyaa : ')

def kabar():
  try:
    ask2 = int(input('Kabarnya gimanaa?(rate 1 - 10) : '))
    if ask2 > 7 :
      print('Alhamdulillah')
    elif 4 < ask2 <= 7:
      print('Tetap semangat')
    else:
      print('Gapapa nanti juga seneng lagi')
  except ValueError:
    print('isi yang bener, pakai angka')
    kabar()

kabar()
time.sleep(1)
print('Nih aku kasih kamu bunga')
time.sleep(1)
print('Kalau mau lihat bunga teken enter')

def teken():
  while True:
    if keyboard.read_key() == 'enter':
      break
    else:
      print('bilangin teken enter')
      teken()
  enterr()

teken()

