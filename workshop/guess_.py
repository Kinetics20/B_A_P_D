#!/usr/bin/python3
from random import randint

num = randint(1, 100)


def guess_number():
    while True:
        try:
            guess_num = int(input('Guess number : '))
            # if guess_num < 1 or guess_num > 100:
            #     print('Entered number is out of range 1-100 , Try again')
            #     continue

        except ValueError:
            print("It's not a number !")
            continue
        if guess_num < 1 or guess_num > 100:
            print('Entered number is out of range 1-100 , Try again')
            continue
        elif guess_num > num:
            print('Entered number is too big , try again : ', num)
        elif guess_num < num:
            print('Entered number is too small , try again : ', num)

        else:
            print('You win', num)
            break


guess_number()
