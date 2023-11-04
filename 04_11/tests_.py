#!/usr/bin/python3

# a = range(0, 11)
# print(a)

ggg = "Is nine a.m at the morning and I'm programming in python"
list_ggg = ggg.split()
print(list_ggg)

my_ggg = " , ".join(list_ggg)
print(my_ggg)

a = range(0, 11)
b = list(a)
print(b)

from random import shuffle
c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
shuffle(c)
print(c[:4])
