#!/usr/bin/python3
import datetime
from random import randint


def d6(num):
    counter = 0
    for _ in range(num):
        counter += randint(1, 6)
    return counter


print(d6(100))


def tomorrow():
    return datetime.date.today() + datetime.timedelta(days=2,weeks=10)


print(tomorrow())
