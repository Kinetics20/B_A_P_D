#!/usr/bin/python3
my_list = [1, 2, 3, 'World', 'Home', 'Toy_car', 3.6]
print('things from my_list: {}'.format(my_list, type(my_list)))

for n in my_list:
    if type(my_list[n]) is not str:
        print(f"value of my_list is integer : {my_list[n]}")
    if type(my_list[n]) is str:
        print(f"value of my_list is sting :  {my_list[n]}")
    else:
        print(f"value of my_list is float :  {my_list[n]}")
