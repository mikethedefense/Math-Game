# To-do list: 
# https://stackoverflow.com/questions/15528939/python-3-timed-input
# Add timed input (For later)
import random
proceed = ""
score = 0
while proceed == "y" or proceed == "":
    try:
        count = random.randint(1,12)
        times_value = random.randint(1,12) 
        result = times_value * count
        print('What is {} times {}:'.format(times_value,count))
        number = input('Please enter a number:')
        number = int(number)
    except ValueError:
        print('Invalid text. Please enter correct digits')
    
    
    if number == result:
        print('You are correct')
        score = score +1
    else:
        print('You are incorrect')
        print('The answer was {}'.format(result))

    print('Your current score is {}'.format(score))
    
    proceed = input("Play again? Y/n:")
   # This test is for children between grades 3 and 6
