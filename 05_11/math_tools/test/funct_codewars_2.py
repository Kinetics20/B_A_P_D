def close_compare(a, b, margin=0):
    # return 0 if not abs(a - b) < margin and not a > b else (1 if not abs(a - b) > margin and not a > b else -1)
    return -1 if a < b and abs(a - b) > margin else (1 if a > b else 0)


# print(close_compare(3, 5, 3))
# print(close_compare(3, 5, 0))
# print(close_compare(2, 5, 3))
# print(close_compare(5, 5, 3))
# print(close_compare(4, 5, ))
# print(close_compare(5, 5, ))
# print(close_compare(6, 5, ))


# test.assert_equals(close_compare(4, 5), -1)
# test.assert_equals(close_compare(5, 5), 0)
# test.assert_equals(close_compare(6, 5), 1
# test.assert_equals(close_compare(2, 5, 3), 0)
# test.assert_equals(close_compare(5, 5, 3), 0)
# test.assert_equals(close_compare(8, 5, 3), 0)
# test.assert_equals(close_compare(8.1, 5, 3), 1)
# test.assert_equals(close_compare(1.99, 5, 3), -1)

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())


print(to_jaden_case('Hello world my new home is far from here'))


def to_jaden_case_1(string):
    return [word.capitalize() for word in string.split()]


# print(to_jaden_case_1('Hello world my new home is far from here'))


def get_count(sentence):
    t = []
    for word in sentence:
        if 'a' in word:
            t.append('a')
        if 'e' in word:
            t.append('e')
        if 'i' in word:
            t.append('i')
        if 'o' in word:
            t.append('o')
        if 'u' in word:
            t.append('u')
    return len(t)


print(get_count('Hello world my new home is far from here'))


def get_count_2(sentence):
    t = []
    for word in sentence:
        for vowel in 'aeiou':
            if vowel in word:
                t.append(vowel)
    return len(t)


def get_count_3(sentence):
    t = [vowel for word in sentence for vowel in 'aeiou' if vowel in word]
    return len(t)


def past(h, m, s):
    return (h * 3600000) + (m * 60000) + (s * 1000)


# print(past(0, 1, 1))

def get_middle(s):
    return s[len(s) // 2 - 1:len(s) // 2 + 1] if not len(s) % 2 else s[len(s) // 2]


print(get_middle('test'))
print(get_middle('testing'))


def abbrev_name(name):
    return '.'.join(word[0].capitalize() for word in name.split())


print(abbrev_name('Sam Harris'))


def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))


print(descending_order(42145))


def DNA_strand(dna):
    new_l = []
    for letter in dna:
        if letter == 'A':
            new_l.append('T')
        elif letter == 'T':
            new_l.append('A')
        elif letter == 'C':
            new_l.append('G')
        elif letter == 'G':
            new_l.append('C')

    return ''.join(new_l)


def DNA_strand_1(dna):
    # return ''.join(['T' if letter == 'A' else 'A' if letter == 'T' else 'G' if letter == 'C' else 'C' for letter in dna])
    return ''.join(
        ['T' if letter == 'A' else 'A' if letter == 'T' else 'G' if letter == 'C' else 'G' for letter in dna])


# print(DNA_strand("AAAA"))
# print(DNA_strand("ATTGC"))
# print(DNA_strand_1("ATTGC"))
# print(DNA_strand("GTAT"))

def basic_op_2(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    else:
        raise ValueError("Nieznany operator")


def basic_op(operator, value1, value2):
    return (
        value1 + value2 if operator == '+' else
        value1 - value2 if operator == '-' else
        value1 * value2 if operator == '*' else
        value1 / value2 if operator == '/' else None
    )


def basic_op_3(operator, value1, value2):
    return eval(f'{value1} {operator} {value2}')


print(basic_op_3('-', 5, 7))


def contains_all_alphabet_letters(s):
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    s_set = set(s.lower())  # Zakładam, że wielkość liter nie ma znaczenia

    return all(letter in s_set for letter in alphabet_set)


def is_pangram(s):
    return True if all(letter in set(s.lower()) for letter in set("abcdefghijklmnopqrstuvwxyz")) else False


# print(is_pangram("The quick brown fox jumps over the lazy dog"))

def has_duplicate_letters_1(s):
    for letter in s:
        if s.count(letter) > 1:
            return True
    return False


def has_duplicate_letters(string):
    return all(string.lower().count(letter) <= 1 for letter in string)


def is_isogram(string):
    return len(set(string.lower())) == len(string)


print(has_duplicate_letters("Dermatoglyphics"))
print(has_duplicate_letters("moose"))
print(has_duplicate_letters("aba"))
print(has_duplicate_letters(""))


def disemvowel(string_):
    # vowels = "AEIOUaeiou"

    return ''.join(char for char in string_ if char not in "AEIOUaeiou")


print(disemvowel("This website is for losers LOL!"))


def some_f(anystr):
    return ' '.join([word[::3] for word in anystr.split()])


print(some_f("Ala ma kota a kot ma ale123"))


def some_f_1(anyint):
    return int(str(anyint)[1:-1])


print(some_f_1(12398765455))


def count_by(x, n):
    new_l = []
    for i in range(x, x * n + 1, x):
        new_l.append(i)
    return new_l


print(count_by(2, 5))


def count_by_2(x, n):
    return [x for x in range(x, x * n + 1, x)]


print(count_by_2(2, 5))


def get_sum(a, b):
    return sum([num for num in range(a, b + 1)])


print(get_sum(-1, 2))


def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


def better_than_average(class_points, your_points):
    return True if len(class_points) / sum(class_points) < your_points else False


def square_sum(numbers):
    return sum([num ** 2 for num in numbers])


print(square_sum([0, 3, 4, 5]))


def find_it(seq):
    return [num for num in seq if seq.count(num) % 2][0]


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))


def sum_two_smallest_numbers(numbers):
    sorted_list = sorted(numbers)
    return sorted_list[0] + sorted_list[1]


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))


def maps(a):
    # return list(set([num * 2 for num in a]))
    return [num * 2 for num in set(a)]


print(maps([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))


def lovefunc(flower1, flower2):
    return (flower1 % 2 == 1 and flower2 % 2 == 0) or (flower1 % 2 == 0 and flower2 % 2 == 1)


print(lovefunc(2, 2))
print(lovefunc(0, 2))
print(lovefunc(168, 328))


def build_tower(n):
    tower = []
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        tower.append(spaces + stars + spaces)

    return tower


def bulid_tower_1(n):
    return [' ' * (n - i - 1) + '*' * (2 * i + 1) + ' ' * (n - i - 1) for i in range(n)]


print(bulid_tower_1(3))


def series_sum(n):
    if n == 0:
        return "0.00"

    total = 0.0
    denominator = 1

    for _ in range(n):
        total += 1 / denominator
        denominator += 3

    return "{:.2f}".format(total)


print(series_sum(1))


def open_or_senior(data):
    return ["Senior" if i >= 55 and k > 7 else "Open" for i, k in data]


def digitize(n):
    return [int(i) for i in str(n)][::-1]


def leo(oscar):
    if oscar == 88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of wallstreet?!"
    elif not (oscar == 88 or oscar == 86) and oscar < 88:
        return "When will you give Leo an Oscar?"
    elif oscar > 88:
        return "Leo got one already!"


# print(leo(100))

def pipe_fix(nums):
    return [num for num in range(nums[0], nums[-1] + 1)]


print(pipe_fix([1, 2, 3, 4, 5, 9]))


def sum_mix(arr):
    return sum(int(i) for i in arr)


# print(sum_mix([9, 3, '7', '3']))


def hero(bullets, dragons):
    return dragons * 2 <= bullets


# print(hero(100, 40))

def cannons_ready(gunners):
    return "Fire!" if all(response == 'aye' for response in gunners.values()) else "Shiver me timbers!"


def shorten_to_date(long_date):
    return " ".join(long_date.split(", ")[:-1])


def correct(s):
    change_s = {'0': 'O', '1': 'I', '5': 'S'}
    return ''.join(change_s.get(char, char) for char in s)


def correct_1(string):
    return string.replace('1', 'I').replace('0', 'O').replace('5', 'S')


def reverse(st):
    # Your Code Here
    return ' '.join(st.split()[::-1])


def correct_polish_letters(st):
    new_dict = {'ą': 'a',
                'ć': 'c',
                'ę': 'e',
                'ł': 'l',
                'ń': 'n',
                'ó': 'o',
                'ś': 's',
                'ź': 'z',
                'ż': 'z'}

    return ''.join(new_dict[letter] if letter in new_dict else letter for letter in st)


print(correct_polish_letters('Władek ślusarz'))

# 01
import statistics


def create_list(i, j):
    return [i, j] * 4


print(create_list(1, 2))
print(create_list(True, False))

# 02

couples_dict = {
    'Alice': 28,
    'Bob': 30,
    'Charlie': 25,
    'Diana': 22,
    'Eve': 35,
    'Frank': 32
}


def list_keys(d):
    temp = []
    for key in d:
        temp.append(key)
    # return temp
    return list(d.keys())
    # return d.values()
    # return d.items()


print(list_keys(couples_dict))

# 03

word_list = ['cat', 'banana', 'carrot', 'dog', 'elephant']


def find_short_words(words):
    temp = []
    for word in words:
        if len(word) < 5:
            temp.append(word)

    return temp


l = find_short_words(word_list)
print(l)

# 04

a_list = [1, 2, 3, 4, 5]


def suma(numbers):
    result = 0
    for number in numbers:
        result += number

    return result


print(suma(a_list))


# 05
def suma_2(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result += number

    return result


print(suma_2(a_list))


# 06
def mean(numbers):
    return statistics.mean(numbers)


print(mean(a_list))


# 07
def mean_2(numbers):
    return sum(numbers) / len(numbers)


print(mean_2(a_list))

size = 5

# 08

for row in range(1, size + 1):
    for columns in range(row):
        print("*", end="")
    print()

for row in range(1, size + 1)[::-1]:
    for columns in range(row):
        print("*", end="")
    print()


# 09

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


def array_madness(a, b):
    return sum([num_a ** 2 for num_a in a]) > sum([num_b ** 3 for num_b in b])


print(array_madness([61], [5, 18, 26, 17, 19, 14, 28, 13, 27]))


def sum_array(arr):
    # return sum(list(set(sorted(arr)))[1:-1])
    return sum(sorted(arr)[1:-1])


print(sum_array([6, 0, 1, 10, 10]))


def sum_array_1(arr):
    return sum(sorted(arr)[1:-1]) if len(arr) > 2 else 0


print(sum_array_1([3, 5]))
print(sum_array_1([5]))
print(sum_array_1([]))


def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"


def rps_1(p1, p2):
    hand = {'rock': 0, 'paper': 1, 'scissors': 2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]


def count_sheeps(sheep):
    # TODO May the force be with you
    return str(sheep).count('True')


def eliminate_sth_in_list(any_list):
    return [item for item in any_list if item is not bool].count(5)


print(eliminate_sth_in_list([True, True, True, False,
                             True, True, 5, True,
                             True, 2, True, False,
                             True, False, False, True,
                             True, 5, True, True,
                             False, False, True, True]))


def summation(num):
    return sum(item for item in range(1, num + 1))


def number(bus_stops):
    sum_index_0 = 0
    sum_index_1 = 0
    for element in bus_stops:
        sum_index_0 += element[0]
        sum_index_1 += element[1]
    return sum_index_0 - sum_index_1


def number_1(bus_stops):
    sum_index_0 = sum(element[0] for element in bus_stops)
    sum_index_1 = sum(element[1] for element in bus_stops)
    return sum_index_0 - sum_index_1


def number_2(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
