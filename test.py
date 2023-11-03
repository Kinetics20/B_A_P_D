#!/usr/bin/python3
my_list = [1, 2, 3, 'World', 'Home', 'Toy_car', 3.6]
# my_list = [100550034324324, 2324324, 132141533, 'World', 'Home', 'Toy_car', 3.6]
for n in my_list:
    if type(n) is str:
        print(f"value of my_list is string : {n}")
    if type(n) is float:
        print(f"value of my_list is float :  {n}")
    if type(n) is int:
        print(f"value of my_list is integer :  {n}")
