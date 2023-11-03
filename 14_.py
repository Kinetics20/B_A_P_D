#!/usr/bin/python3
# n = "Where is my home"
#
# for i in n:
#     print(f"letters_from_string : {i}")
#
# k = 0
# while k < len(n):
#     list(n)
#     print(n[k])
#     k += 1

# a = input("Input sth : ")
# print(f"Entered number is : {a}")
#
# b = 100 / 33
# print(f"integer of b is : {int(b)}")

# from random import randint
#
#
# rnd = randint(10, 20)
#
# my_str = "What you're gonna do with it ?"
# my_list = my_str.split()
# # d = list(my_str)
# print(my_list)
# my_str_2 = " : ".join(my_list)
# print(f"Elements od string : {my_str_2}")
# print(my_str.upper())
# print(my_str.lower())

# from random import randint
#
# rnd = randint(10, 230)

a = range(0, 10)
b = list(a)
# print(b, end=" ")

# from random import shuffle
#
# shuffle(b)
# print(b[:5])

def my_sum(x, y):
    z = x +y
    return z
num_1 =  50
num_2 = 100
num_sum = my_sum(num_1, num_2)
print(f"Sum of numbers {num_1} and {num_2} is {num_sum}")