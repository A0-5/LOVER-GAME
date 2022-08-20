# importing colors module
from colors import *
# importing random module
from random import randint

# Welcome screen
print(YELLOW, '**** Welcome TO LOVER-GAME ****')
user_input = int(input(WHITE + '1. Start Game\n'
                               '2. About Lover-Game\n'
                               '3. Exit Application\n\n'
                               'Choose an option above : '))


# determine user input
if user_input == 1:
    user_input =int(input(WHITE + 'Choose Game Level\n'
                                 '1. Lazy (1-100)\n'
                                 '2. Intermediate (1-500)\n'
                                 '3. Hard (1- 1000)\n\n'
                                 'Provide Level:   '))

    #Determine the guess range

    guess_range = 0
    if user_input == 1:
       guess_range = 100
    elif user_input == 2:
       guess_range = 500
    elif user_input == 3:
        guess_input = 1000

    #   generate random number base on the guess range
    generated_number = randint(1, guess_range)
# user guessing attempt
    user_chance = 3
    for chance in range(3):
        user_guess = int(input(WHITE + 'Provide Your Guess NUMBER :'))

    #        Determine/Validatate User Guess
        if user_guess == generated_number:
           print(GREEN, f'Congrat!! You Guessed {generated_number} Right')
           break
        elif user_guess > generated_number:
            print(YELLOW, f'{user_guess}Too High, Try Again!!')
            user_chance -= 1
        elif user_guess < generated_number:
            print(YELLOW, f'{user_guess}Too Low, Try Again!!!')
            user_chance -= 1

    if user_chance < 1:
        print(RED, f'You Failed, Try Again!!!!\n'
                   f'The Correct Guess Number is {generated_number}')



    elif user_input == 2:
        print(YELLOW, 'Loving Guessing Number.')
    elif user_input == 3:
        print(WHITE, 'Hope To Use You Again Gamer.')
        exit(10)
    else:
        print(RED, 'Invalid Option, Try Again!!!')
