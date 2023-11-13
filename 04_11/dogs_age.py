#!/usr/bin/python3

from random import randint


def dogs_age_1(age):
    dogs_age_y = age * 10.5
    return dogs_age_y


def dogs_age_2(age):
    dogs_age_o = 21 + (age - 2) * 4
    return dogs_age_o


num_1 = float(input("Enter the age of dog : "))
if num_1 <= 2:
    age_of_dog = dogs_age_1(num_1)
    print(f"dog's age is : {age_of_dog}")
if num_1 > 2:
    age_of_dog = dogs_age_2(num_1)
    print(f"dog's age is : {age_of_dog}")


def dogs_age_3():
    age = randint(1, 14)
    if age < 2:
        return age * 10.5
    else:
        return 21 + (age - 2) * 4


print(dogs_age_3())
