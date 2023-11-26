#!/usr/bin/python3

# 01

# def chessboard(n):
#     idx = 0
#
#     for _ in range(n):
#         if not idx % 2:
#             print("# " * (n // 2))
#         else:
#             print(" #" * (n // 2))
#         idx += 1
#
#
# chessboard(10)
#

# 01

def make_tuple(a, b, c=3, d=4):
    return (a, b, c, d)


print(make_tuple("mama", "father"))
print(make_tuple("mama", "father", "fish", "10"))
print(make_tuple(0, 0, 0, 0))


# 02

def find_first_and_last(my_):
    temp = []
    for item in my_[0]:
        temp.append(item)
    for item in my_[-1]:
        temp.append(item)
    return tuple(temp)


mixed_list = ["1.68", 1.5, 'dwa', 3, 'cztery', 5, 6.0, 'siedem', 8, "5469"]
mixed_tuple = ('a', 'b', 'c', 'd', 'e')
print(find_first_and_last(mixed_list))
print(find_first_and_last(mixed_tuple))


def find_first_and_last_2(my_collection):
    if not my_collection:
        return None
    first_element = my_collection[0]
    second_element = my_collection[-1]
    return (first_element, second_element)


mixed_list_1 = [1.68, 1.5, 'dwa', 3, 'cztery', 5, 6.0, 'siedem', 8, 5469]
mixed_tuple_2 = (25.5, 'b', 'c', 'd', 25.898)
print(find_first_and_last_2(mixed_list_1))
print(find_first_and_last_2(mixed_tuple_2))


# 03
def format_date(day, month, year):
    if month < 1 or month > 12:
        return None
    if month in {1, 3, 5, 7, 8, 10, 12}:
        if day < 1 or day > 31:
            return None
    elif month in {2, 4, 6, 9, 11}:
        if day < 1 or day > 30:
            return None
    elif month == 2:
        if day < 1 or day > 28:
            return None
    elif year <= 0:
        return None

    return f"{day}, {month}, {year}"


print(format_date(12, 4, 2008))
print(format_date(12, 50, 2008))
print(format_date(12, 50, -2008))


# 05

def censor(any_str):
    new_list = []
    forbid_list = ['Java', 'C#', 'Ruby', 'PHP']
    words = any_str.split()
    for _ in words:
        if _ in forbid_list:
            new_list.append('****')
        else:
            new_list.append(_)
    return " ".join(new_list)


my_str = 'I like Java but I prefer python and sometimes I like Ruby'
print(censor(my_str))


# 04

def find_boundaries_2(any_list):
    if not any_list:
        return
    new_list = [value for value in any_list if isinstance(value, (int, float))]

    return min(new_list), max(new_list)


m_list = [1, 2, 3.14, 3, 42]
m_list_2 = []
m_list_3 = [-1, 2, 3.14, 3, 80, 'Home', 'Theatre', 'Oracle']

print(find_boundaries_2(m_list))
print(find_boundaries_2(m_list_2))
print(find_boundaries_2(m_list_3))

# 06

def check_palindrome_2(chain_str):
    temp = chain_str.split()
    for index in temp:
        if index == index[::-1]:
            return True
    return False


print(check_palindrome_2('ma kota ala'))
