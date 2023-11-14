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

# 08

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

# 09

mixed_list_2 = [42, 3.14, "hello", True, [1, 2, 3], {'key': 'value'}, None, (4, 5), 'world', False]


def create_list_last_3_index(items):
    new_list = []
    for item in items[:-4:-1]:
        new_list.append(item)
    return new_list


print(f'The new list made up of last three indexes of mixed list :\n{create_list_last_3_index(mixed_list_2)}')

# 10

any_str = "Things are not always what they seem"


def create_str_to_list(my_str):
    return my_str.split()


print(create_str_to_list(any_str))

new_list_2 = ['Things', 'are', 'not', 'always', 'what', 'they', 'seem']


def create_list_to_str(t):
    return " ".join(t)


print(create_list_to_str(new_list_2))


def bmi(mass, height):
    return mass / height ** 2


def capitalize(text):
    return text.capitalize()


def casefold_string(text):
    return text.casefold()


def checktype(a):
    return type()


def sort(arr):
    return sorted(arr)


def center_string(text):
    return text.center(20)


def count_apples(text):
    return text.count('apples')


def encode_string(text):
    return text.encode


print(encode_string('Ala ma kota'))


def check_endswith(text):
    return text.endswith('.')


def expand_text(text):
    return text.expandtabs(23)


def find_pear(text):
    return text.find('apple')


def text_index(text):
    return text.index('root')


def check_alphanumeric(text):
    return text.isalnum()


def check_letters(text):
    return text.isalpha()


def check_ascii(text):
    return text.isascii()


def check_decimal(text):
    return text.isdecimal()


def check_digit(text):
    return text.isdecimal()


def check_digital(text):
    return text.isdigital()


def check_lower(text):
    return text.islower()


def check_numeric(text):
    return text.isnumeric()


def check_printable(text):
    return text.isprintable()


def check_space(text):
    return text.isspace()


def check_if_tittle(text):
    return text.istittle()


def check_if_upper(text):
    return text.isupper()


def text_join(tup):
    return "#".join(tup)


new_list_3 = ['Things', 'are', 'not', 'always', 'what', 'they', 'seem', 5, 6, 8]


# def fill_to_new_list(any_list):
#     temp = []
#     for item in any_list['Things', 'always', 5, 6, 8]:
#         temp.append(item)
#     return temp
#
#
# print(fill_to_new_list(new_list_3))


def fill_to_(any_list):
    temp = []
    temp.append(any_list[1])
    temp.append(any_list[6])
    temp.append(any_list[7])
    temp.append(any_list[9])
    return temp


print(fill_to_(new_list_3))

# for index in indexes:
#     temp.append(any_list[index])

new_list_4 = ['Things', 'are', 'not', 'always', 'what', 'they', 'seem', 5, 6, 8, 20, 60]


def fill_to_n_(any_list):
    temp = []
    indexes = [0, 5, 6, 8]
    for index in indexes:
        temp.append(any_list[index])
    return temp


print(fill_to_n_(new_list_4))

my_dict_10 = {
    'name': 'John Doe',
    'age': 25,
    'city': 'Anytown',
    'is_student': False
}


# return dict_1.keys()
# return dict_1.values()

def create_list_from_dict(any_dict):
    temp_key = []
    temp_values = []
    index_key = any_dict.keys()
    index_values = any_dict.values()
    for index_k in index_key:
        temp_key.append(index_k)
    for index_v in index_values:
        temp_values.append(index_v)
    return temp_key, temp_values


print(create_list_from_dict(my_dict_10))
