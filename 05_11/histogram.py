#!/bin/usr/python3

# def histogram(any_list):
#     for row in any_list:
#         for _ in range(row):
#             print('#', end="")
#         print()
#     if any(isinstance(element, str) for element in any_list):
#         return None
#
#
# my_list = [1, 2, 3, 4, 10, 15, 40]
# # my_list_2 = [1, 2, 3, 4, 10, 15, 40, "What's up"]
# print(histogram(my_list))


def histogram_2(any_list):
    if any(isinstance(element, str) for element in any_list):
        return None
    else:
        for row in any_list:
            for _ in range(row):
                print('#', end="")
            print()
    return " "


my_list_2 = [1, 2, 3, 4, 10, 15, 40, "What's up"]
print(histogram_2(my_list_2))
my_list = [1, 2, 3, 4, 10, 15, 40]
print(histogram_2(my_list))


# if any(isinstance(element, str) for element in any_list):
#     return None

# def build_tree(i, j):
#     for i in range(1, size + 1):
#         for j in range(i):
#             print("*", end="")
#         print()
#     return "|"
#
# print(build_tree(size, size + 1))

def check_list_str(any_list):
    new_list_num = []
    new_list_str = []

    for index in any_list:

        if isinstance(index, (int, float)):
            new_list_num.append(index)
        else:
            new_list_str.append(index)

    return new_list_str, new_list_num


mixed_list = [42, 'apple', 3.14, 'banana', 7, 'orange', 99.9, 'grape', 123, 'kiwi', 5.5, 'dog', 1, 'cat', 2.718, 'bird',
              77, 'elephant', 8.8, 'monkey']
print(check_list_str(mixed_list))


def histogram_n_2(any_list):
    if isinstance(any_list, (int, float)):
        for index in range(1, any_list + 1):
            for _ in range(any_list):
                print('#', end="")
            print()
    return None


print(histogram_n_2(mixed_list))
print(histogram_n_2(my_list))

my_list_2 = [1, 2, 3, 4, 10, 15, 40, "What's up"]

for i in range(1, len(my_list_2) + 1):
    print(i, my_list_2[i - 1])

my_list_3 = [10 * i for i in range(0, 11)]

print(my_list_3)

my_list_3 = [i for i in range(0, 11) if not i % 5]
print(my_list_3)

my_str_3 = "".join(map(str, my_list_3))

print(my_str_3)
t = my_str_3.split()
print(t)
t_l = list(my_str_3)
