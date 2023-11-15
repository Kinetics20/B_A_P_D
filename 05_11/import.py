#!/usr/bin/python3
import calendar
import datetime
import random
from calendar import weekday, day_name
from random import randint, choice

# to jest do importu z pliku :
from to_import import create_list, word_list


def d6(num):
    counter = 0
    for _ in range(num):
        counter += randint(1, 6)
    return counter


print(d6(100))


def tomorrow():
    return datetime.date.today() + datetime.timedelta(days=2, weeks=10)


print(tomorrow())

message = create_list()
print(message)

my_birthday = weekday(1974, 4, 12)
print(f"My birthday is on : {day_name[my_birthday]}")


# word_r = randint(word_list)
# print(word_r)

def draw_from_list(any_list):
    return choice(any_list)


print(draw_from_list(word_list))
