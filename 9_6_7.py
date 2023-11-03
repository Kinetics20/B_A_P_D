#!/usr/bin/python3
def add(x , y ):
    return x + y
def substraction(x ,y):
    return x - y
def multiply(x ,y):
    return x * y
def division(x ,y):
    return x / y

num_1 = float(input("enter the first number : "))
print(" ")
num_2 = float(input("enter the second number : "))
print(" ")
print("calculation options :")
print(" ")
print("1 - addition")
print("2 - substraction")
print("3 - multiplication")
print("4 - division")
print(" ")

while True:
    num = int(input("choice specific math function 1 / 2 / 3 / 4 : "))
    if num == 1:
        print("the score is : " , add(num_1,num_2))
        break
    elif num == 2:
        print("the score is : " , substraction(num_1,num_2))
        break
    elif num == 3:
        print("the score is : " , multiply(num_1,num_2))
        break
    elif num == 4:
        print("the score is : " , division(num_1,num_2))
        break
    else:
        print("Wrong choice , select corect number of math function !")