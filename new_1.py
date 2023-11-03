#!/usr/bin/python3

# a = "home sweat home !!!"
# print(f"it's inside {a}")

new_list = []
num = int(input("Enter number of repetition : "))
for t in range(num):
    g = int(input("Enter number : "))
    new_list.append(str(g))

print(f"List elements : {' , '.join(new_list)}")
# print("elementy listy :{}".format(" ".join(new_list)))
print(f"element : {new_list[0]} is a type of {type(new_list[0])}")

new_list_2 = []
for d in new_list:
    new_list_2.append(int(d))
print(f"new element {new_list_2[0]} is type of : {type(new_list_2[0])}")

len_new_list_2 = len(new_list_2)

if len_new_list_2 > 5:
    print(f"length of new_list_2 is higher than : {len_new_list_2}")
if len_new_list_2 < 5:
    print(f"length of new_list_2 is lower than : {len_new_list_2}")
