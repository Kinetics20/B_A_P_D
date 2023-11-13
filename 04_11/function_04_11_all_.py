#!/usr/bin/python3
from random import randint

# 01

no_of_stars = randint(1, 20)


def amount_of_stars(num):
    return num * "*"


print(f"drawn number : {no_of_stars} amount of stars : {amount_of_stars(no_of_stars)}")

# 02

rows = randint(5, 15)
columns = randint(5, 15)


def create_square(i, j):
    for row in range(i):
        print(j * "*")


print(f"rows : {rows} , columns : {columns})")
create_square(rows, columns)

# 03

size = randint(3, 9)

print(size)


def build_tree(i, j):
    for i in range(1, size + 1):
        for j in range(i):
            print("*", end="")
        print()
    return "|"


print(build_tree(size, size + 1))


# 04

def square(num):
    return num ** 2


print(square(100))


# 05

def multiply(subject, times):
    return subject * times


print(multiply(5, 20))
print(multiply(5, "20"))


# 06

def power(base, exponent):
    return base ** exponent


print(power(2, 3))


# 07

def convert_to_usd(euros):
    return 0.82 * euros


print(convert_to_usd(100))


# 08
def count_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print(count_to_celsius(75))


# 09

def calculate_net(gross, vat):
    return gross / (1 + vat / 100)


print(calculate_net(123, 23))


# 10

def is_even(number):
    if number % 2:
        return False
    return True


print(is_even(4))
print(is_even(9))
print(is_even(12))

# 10_1 simpliest
print()


def is_even_2(number):
    return False if number % 2 else True


print(is_even_2(8))
print(is_even_2(11))
print(is_even_2(835))


# 10_3

def is_even_3(number):
    return not number % 2


print(is_even_3(835))
print(is_even_3(800))


# 11 for
def iterate_through(number):
    for item in range(1, number + 1):
        print(f"number : {item}, is number even ? ,{is_even(item)} ")


iterate_through(42)


# 11 while

def iterate_through_2(number):
    counter = 1
    while counter <= number:
        print(f"number : {number}, is number even ? ,{is_even(number)} ")
        counter += 1


iterate_through(19)

# 12
def iterate_through_4(number):
    counter = 1
    while counter <= number:
        counter += 1
        # print(f"Number is : {counter} is it even ? : {is_even(counter)}")
        print(f"Number is : {counter} is it even ? : ,  {'even' if is_even(counter) else 'Odd'} ")


iterate_through_4(21)
