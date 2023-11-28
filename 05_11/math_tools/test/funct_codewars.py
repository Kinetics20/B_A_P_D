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


# if __name__ == '__main__':
#     print(roll(3, 8, -2))


def count_score_2(any_str):
    new_list = [int(point) for point in any_str if point.isdigit()]
    return '3' if new_list[0] > new_list[1] else ('0' if new_list[0] < new_list[1] else '1')


# print(count_score_2('1:3'))
# print(count_score_2('4:3'))
# print(count_score_2('3:3'))


def count_score_3(any_list):
    new_list = [int(point) for item in any_list for point in item if point.isdigit()]
    return new_list


# print(count_score_3(['1:0', '2:0', '3:0']))

def count_sth_(any_list):
    new_list = []
    for result in any_list:
        a, b = map(int, result.split(':'))
        if a > b:
            new_list.append(3)
        elif a < b:
            new_list.append(0)
        else:
            new_list.append(1)
    return sum(new_list), new_list
    # return a, b


# print(count_sth_(['1:0', '2:0', '3:0']))


def create_list_str_to_list_int(any_list):
    return list(map(int, any_list))


print(create_list_str_to_list_int(['1', '2', '3', '4']))


def findNeedle(haystack):
    i_of_needle = haystack.index('needle')
    if 'needle' in haystack:
        # i_of_needle = haystack.index('needle')
        return f'found the needle at position {i_of_needle}'


needle_list = ['needle', 'haystack', 'another', 'finding', 'no', 'here']

print(findNeedle(needle_list))


def find_needle_index(needle_list):
    return needle_list.index('needle') if 'needle' in needle_list else "Needle not found in the list."


print(find_needle_index(needle_list))


def uni_total(s):
    return sum(ord(character) for character in s)


print(uni_total('ala ma kota'))


def extra(any_list):
    new_list = []
    for unit in any_list:
        new_list.append(unit)
    new_list.append(len(any_list))
    return new_list


def extra_2(any_list):
    return any_list + [len(any_list)]


print(extra_2([1, 2]))
print(extra_2([]))


def count_age(age):
    if age > 14:
        min_ = int((age / 2) + 7)
        max_ = int((age - 7) * 2)
    else:
        min_ = int(age - 0.10 * age)
        max_ = int(age + 0.10 * age)
    return f"{min_}-{max_}"


def count_age_2(age):
    return f"{int((age / 2) + 7)}-{int((age - 7) * 2)}" if age > 14 else f"{int(age - 0.10 * age)}-{int(age + 0.10 * age)}"


print(count_age(27))
print(count_age(5))
print(count_age(17))


def feast(beast, dish):
    return True if beast[0] == dish[0] and beast[-1] == dish[-1] else False


print(feast('ala ma kota', 'az ma kota'))
