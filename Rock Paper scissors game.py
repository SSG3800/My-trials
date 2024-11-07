print('-----------------------------------')
print('WELCOME TO ROCK PAPER SCISSORS GAME')
print('-----------------------------------')

import random

user_score = 0
computer_score = 0

start_key = input("Are You Ready (y/n) :").lower()

items = ['rock','paper','scissor']

while True:

    if start_key == 'n':
        break

    elif start_key == 'y':

        user_input = input("Choose the item (rock ,paper,scissor)[[press q to exit]] : ").lower()

        random_item = random.choice(items)

        if user_input == random_item :
            print(f"I'm Also Choose {random_item} one ")
            print('So that is a DRAW')

        elif user_input == 'rock' and random_item ==  'paper' :
            print("Yes I win , I choose Paper and You choose Rock ")
            computer_score += 1

        elif user_input == 'rock' and random_item ==  'scissor' :
            print("Wow you are Amazing , you win , I choose scissor and You choose Rock ")
            user_score += 1

        elif user_input == 'paper' and random_item ==  'scissor' :
            print("Yes I win , I choose scissor and You choose paper ")
            computer_score += 1

        elif user_input == 'paper' and random_item ==  'rock' :
            print("Wow you are Amazing , you win , I choose Rock and You choose Paper ")
            user_score += 1

        elif user_input == 'scissor' and random_item == 'rock':
            print("Yes I win , I choose Rock and You choose scissor ")
            computer_score += 1

        elif user_input == 'scissor' and random_item ==  'paper' :
            print("Wow you are Amazing , you win , I choose Paper and You choose Scissor ")
            user_score += 1

        elif user_input == 'q':
            break

print('*****************************')
print(f'Your score is    : {user_score}')
print(f'Computer Score is: {computer_score}')
if user_score > computer_score:
    print('You Win')
elif computer_score > user_score:
    print('Computer win')
elif computer_score == user_score:
    print('Draw')
print('*****************************')

print('---------------------------------------------')
print('That is a good game lets play in another time')
print('---------------------------------------------')







