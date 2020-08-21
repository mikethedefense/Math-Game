# Math game project

# Imports
import random
from threading import *
import threading
import sys
import time

# Variables
timer = 10
t = Timer(timer, print, ["\n Sorry time is up"])
score = 0
flag = True

# Before start of game
def start_thread():
    time.sleep(10)
    global flag
    flag = False

print("You have", timer, "seconds to respond to these multiplication questions")
s = threading.Thread(target = start_thread)
s.start()
t.start()

# Main game loop
while flag == True:
    try:
        count = random.randint(1,12)
        times_value = random.randint(1,12) 
        result = times_value * count
        print('What is {} times {}:'.format(times_value,count))
        number = input('Please enter a number:')
        number = int(number)
    except ValueError:
        print('Invalid text. Please enter correct digits')
        continue
   
    if number == result:
        print('You are correct')
        score += 1
    else:
        print('You are incorrect')
        print('The answer was {}'.format(result))
        print('Your current score is {}'.format(score))

# End of the game
t.cancel()
print("Your score:", score)
