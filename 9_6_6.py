<<<<<<< HEAD
#!/usr/bin/python3
=======
>>>>>>> aa6a68e26549040403c7e8507dc933706c55d893
def add(x ,y):
    return x + y
def substraction(x ,y):
    return x - y
def multiply(x ,y):
    return x * y
def division(x ,y):
    return x / y

print(" ")
print("calculation options :")
print(" ")
print("1 - addition")
print("2 - substraction")
print("3 - multiplication")
print("4 - division")
print(" ")



choice = float(input("enter specific number of maths operations 1/2/3/4 : "))
print(" ")
num_1 = float(input("enter the first number : "))
num_2 = float(input("enter the second number : "))
print(" ")
if choice == 1:
    print(num_1 , "+" , num_2 , "=" , add(num_1,num_2))

else:
    print("entered choice is invalid ")