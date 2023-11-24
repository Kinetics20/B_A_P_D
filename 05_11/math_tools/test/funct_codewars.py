from random import randint
from sys import getsizeof


def add_length(str_):
    return [(str(word) + " " + str(len(word))) for word in str.split(str_)]


# print(add_length('My home was in the distance six miles from my work'))


def is_digit(any_value):
    return True if isinstance(any_value, (int, float)) else False


# print(is_digit(3.7))
# print(is_digit(3))
# print(is_digit("3"))

def square_root(any_int_list):
    try:
        new_list = []
        for num in any_int_list:
            if (num ** 0.5).is_integer():
                new_list.append(int(num ** 0.5))
            else:
                new_list.append(num ** 2)
        return new_list
    except AttributeError:
        print('List includes value under the zero , enter the list with natural numbers ')

    except TypeError:
        print('List includes string value , enter the list without string')


# print(square_root([-4, 3, 9, 7]))
# print(square_root(['Mike', 3, 9, 7]))


def count_bytes(any_variable):
    return getsizeof(any_variable)


# if __name__ == '__main__':
#     print(count_bytes('user'))
#     print(count_bytes([1, 2, 3]))
#     print(count_bytes((1, 8, 9)))


def roll(dices, dice_type=6, modifier=0):
    if dice_type not in (3, 4, 6, 8, 10, 12, 100):
        raise Exception('No such dice')
    return sum(randint(1, dice_type) for _ in range(dices)) + modifier


if __name__ == '__main__':
    print(roll(3, 8, -2))
