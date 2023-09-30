import random
import os

def questions():
    numbers = [1,2,3,4,5,6,7,8,9,0]
    quiz = ''

    for number in range(4):
        get = random.choice(numbers)
        quiz += str(get)
        place = numbers.index(get)
        numbers.pop(place)
    return quiz   

def player_answer():
    print('[!] The input you provide must contain 4 numbers')
    answer = str(input('Masukan Input : '))
    if len(answer) != 4:
       return player_answer()
    else:
       return answer
    
def output(history):
    os.system('cls')
    show_header = '|  Answer  |  Correct Number  |  Correct Place  |'
    border = '+----------+------------------+-----------------+'
    show = ''
    for x in range(len(history['answer'])):
        y = 4
        for key,value in history.items():
            show += '|'
            show += value[x].center(len(key)+y)
        show += '|\n'
    print(border)
    print(show_header)
    print(border)
    print(show.rstrip())
    print(border)

def game():
    life = 8
    question = questions()
    history = {
       'answer' : [],
       'correct_number' : [],
       'correct_place' : []
    }

    while life != 0:
        correct_number = 0
        correct_place = 0
        
        answer = player_answer()

        if answer == question:
            return 'You Win!!!'
        else:
            life -= 1
            
        for each in answer:
          if each in question:
            correct_number += 1
        for place in range(4):
          if answer[place] == question[place]:
              correct_place += 1

        history['answer'].append(answer)
        history['correct_number'].append(str(correct_number))
        history['correct_place'].append(str(correct_place))

        output(history)

    print(f'Right Numbers : {question}')

if __name__ == '__main__':
    game()
      
        

