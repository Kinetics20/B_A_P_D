#!/usr/bin/python3
import statistics


# 01

def chessboard(n):
    idx = 0

    for _ in range(n):
        if not idx % 2:
            print("# " * (n // 2))
        else:
            print(" #" * (n // 2))
        idx += 1


chessboard(10)


# 02

def create_list(idx_1, idx_2):
    return [idx_1, idx_2] * 2


print(create_list(5, 6))
print(create_list(False, True))


# 03

def list_keys(dict_1):
    list_key = []
    for key in dict_1:
        list_key.append(key)
    # return list_key
    # return dict_1.keys()
    # return dict_1.values()
    # return dict_1.items()
    return list(dict_1.keys())


mixed_dict = {
    "integer_value": 42,
    "float_value": 3.14,
    "string_value": "Hello, World!",
    "another_integer": 123,
    "another_float": 2.718,
    "another_string": "Python"
}

print(list_keys(mixed_dict))


# 04

def find_short_words(any_list):
    empty_list = []
    for item in any_list:
        if len(item) < 5:
            empty_list.append(item)
    return empty_list


str_list = ["apple", "banana", "orange", "grape", "pear", "kiwi"]
print(find_short_words(str_list))

# 05

num_list = [3, 1.5, 7, 2.8, 5, 4.2]


def suma(numbers):
    count = 0
    for item in numbers:
        count += item
    return count


print(suma(num_list))


# 06

def mean(numbers):
    return statistics.mean(numbers)


print(mean(num_list))


# 07

def mean_2(numbers):
    return sum(numbers) / len(numbers)


print(mean_2(num_list))


def check_odd(number):
    return 'Odd' if number % 2 else 'Even'


print(check_odd(2))

# 10

mixed_list = [42, 3.14, "hello", 7, 2.718, "world", 10]


def check_val_list(items):
    new_list = []
    new_list_str = []
    new_list_int = []
    for item in items:
        if isinstance(item, float):
            new_list.append(item)
        if isinstance(item, str):
            new_list_str.append(item)
        else:
            new_list_int.append(item)
    return new_list, new_list_str, new_list_int


print(check_val_list(mixed_list))

# 11

mixed_list_2 = [42, 3.14, "hello", True, [1, 2, 3], {'key': 'value'}, None, (4, 5), 'world', False]


def create_list_last_3_index(items):
    new_list = []
    for item in items[:-4:-1]:
        new_list.append(item)
    return new_list


print(f'The new list made up of last three indexes of mixed list :\n{create_list_last_3_index(mixed_list_2)}')
