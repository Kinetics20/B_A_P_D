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


def number_3(bus_stops):
    sum = 0
    for i in bus_stops:
        sum += i[0] - i[1]
    return sum


from functools import reduce


def grow(arr):
    return reduce(lambda x, y: x * y, arr)


def grow_1(arr):
    product = 1
    for i in arr:
        product *= i
    return product


def powers_of_two(n):
    return [2 ** num for num in range(0, n + 1)]


def how_much_i_love_you(nb_petals):
    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]

    index = (nb_petals - 1) % len(phrases)

    return phrases[index]


def find_multiples(integer, limit):
    return [num for num in range(integer, limit + 1) if not num % integer]


def count_squares(cuts):
    return (cuts + 1) ** 3 - (cuts - 1) ** 3


def count_squares_1(x):
    return 6 * x ** 2 + 2


def sort_array(source_array):
    return sorted(item for item in source_array if item % 2)


print(sort_array([5, 8, 6, 3, 4]))


def sort_array_2(source_array):
    odd_numbers = sorted(item for item in source_array if item % 2)
    return [even if even % 2 == 0 else odd_numbers.pop(0) for even in source_array]


def well(x):
    return 'Fail!' if x.count('good') == 0 else 'Publish!' if x.count('good') <= 2 else 'I smell a series!'


def well_2(x):
    if x.count('good') == 0:
        return 'Fail!'
    elif x.count('good') <= 2:
        return 'Publish!'
    else:
        return 'I smell a series!'


def cube_checker(volume, side):
    return abs(volume ** (1 / 3) - side) < 1e-10 if volume > 0 and side > 0 else False


def simple_multiplication(number):
    return 8 * number if not number % 2 else 9 * number


def rot13(message):
    result = ''
    for char in message:
        if char.isalpha():
            shift = 13 if char.islower() else -13
            result += chr(
                (ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
        else:
            result += char
    return result


def duplicate_encode(word):
    word = word.lower()
    return ''.join([')' if word.count(char) > 1 else '(' for char in word])


def collinearity(x1, y1, x2, y2):
    return x1 * y2 == x2 * y1


def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and pin.isdigit()


def validate_pin_2(pin):
    return len(pin) in [4, 6] and pin.isdigit()


def set_alarm(employed, vacation):
    return employed and not vacation


def string_to_array(s):
    return s.split() or ['']


def string_to_array_2(string):
    return string.split(" ")


def switch_it_up(number):
    numbers_dict = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    if number in numbers_dict:
        return numbers_dict[number]


def switch_it_up_1(n):
    return ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][n]


def switch_it_up_3(number):
    dict = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        0: "Zero"}

    return dict.get(number)


def domain_name(url):
    url = url.split("//")[-1]

    if url.startswith("www."):
        url = url[4:]

    url = url.split("/")[0]

    if "." in url:
        parts = url.split(".")
        if len(parts) > 2:
            if parts[-1] in ["com", "net", "org", "jp", "za", "uk"]:
                url = parts[-3]
            else:
                url = parts[-2]
        else:
            url = parts[0]

    return url


def domain_name_1(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


def tribonacci_1(signature, n):
    if n == 0:
        return []
    elif n <= len(signature):
        return signature[:n]
    else:
        result = signature[:]
        for i in range(n - len(signature)):
            next_term = sum(result[-3:])
            result.append(next_term)
        return result


def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res


def printer_error(s):
    error_count = sum(1 for char in s if char > 'm')
    return f"{error_count}/{len(s)}"


def invert(lst):
    return [-x for x in lst]


def define_suit(card):
    if 'C' in card:
        return 'clubs'
    if 'D' in card:
        return 'diamonds'
    if 'H' in card:
        return 'hearts'
    if 'S' in card:
        return 'spades'


def define_suit_1(card):
    d = {'C': 'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}
    return d[card[-1]]


def define_suit_2(card):
    return {'C': 'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}[card[-1]]


def ensure_question(s):
    return s + '?' if not s.endswith('?') else s


def ensure_question_2(s):
    return s if s.endswith('?') else s + '?'


def ice_brick_volume(radius, bottle_length, rim_length):
    return (((2 * radius) ** 2) * (bottle_length - rim_length)) / 2


def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))


def count_smileys(arr):
    return sum([1 for sign in arr if
                len(sign) == 2 and sign[0] in (':', ';') and sign[1] in (')', 'D') or len(sign) == 3 and sign[0] in (
                    ':', ';') and sign[1] in ('-', '~') and sign[2] in (')', 'D')])


def duck_duck_goose(players, goose):
    return players[(goose - 1) % len(players)].name


def same_case(a, b):
    if not a.isalpha() or not b.isalpha():
        return -1
    elif a.islower() == b.islower() or a.isupper() == b.isupper():
        return 1
    else:
        return 0


def same_case_1(a, b):
    return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1


def min_max(lst):
    return [min(lst), max(lst)]


def sum_dig_pow(a, b):
    def is_eureka(num):
        digits = [int(digit) for digit in str(num)]
        return num == sum(digit ** (index + 1) for index, digit in enumerate(digits))

    return sorted(num for num in range(a, b + 1) if is_eureka(num))


def dig_pow(n):
    return sum(int(x) ** y for y, x in enumerate(str(n), 1))


def sum_dig_pow_2(a, b):
    return [x for x in range(a, b + 1) if x == dig_pow(x)]


def sum_dig_pow_3(a, b):
    return [x for x in range(a, b + 1) if sum(int(d) ** i for i, d in enumerate(str(x), 1)) == x]


def flick_switch(lst):
    switch = True
    return [switch := not switch if word == 'flick' else switch for word in lst]


def multiply(n):
    return n * 5 ** len(str(abs(n)))


def take(arr, n):
    return arr[:n]


def usdcny(usd):
    return f"{round(usd * 6.75, 2)} Chinese Yuan"


def usdcny(usd):
    return f"{round(usd * 6.75, 2):.2f} Chinese Yuan"


def hello(name=""):
    return "Hello, World!" if not name else f'Hello, {name.capitalize()}!'


def greet(language):
    dictionary = {
        "english": "Welcome",
        "czech": "Vitejte",
        "danish": "Velkomst",
        "dutch": "Welkom",
        "estonian": "Tere tulemast",
        "finnish": "Tervetuloa",
        "flemish": "Welgekomen",
        "french": "Bienvenue",
        "german": "Willkommen",
        "irish": "Failte",
        "italian": "Benvenuto",
        "latvian": "Gaidits",
        "lithuanian": "Laukiamas",
        "polish": "Witamy",
        "spanish": "Bienvenido",
        "swedish": "Valkommen",
        "welsh": "Croeso"
    }
    return dictionary.get(language, 'Welcome')


def get_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None


def get_key_1(dictionary, value):
    return next((key for key, val in dictionary.items() if val == value), None)


def include(arr, item):
    return item in arr


def each_cons(lst, n):
    return [lst[i:i + n] for i in range(len(lst) - n + 1)]


def merge_arrays(arr1, arr2):
    return list(sorted(set(arr1 + arr2)))


def mouth_size(animal):
    return 'small' if animal.lower() == 'alligator' else 'wide'


def is_digit(n):
    return len(n) == 1 and n.isdigit() and int(n) in range(0, 10)


def to_freud(sentence):
    return '' if not sentence else ' '.join("sex" for item in sentence.split())


def string_clean(s):
    return ''.join(char for char in s if not char.isdigit())


def pythagorean_triple(integers):
    integers.sort()
    return integers[0] ** 2 + integers[1] ** 2 == integers[2] ** 2


def two_sum(numbers, target):
    num_indices = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in num_indices:
            return (num_indices[complement], i)
        num_indices[num] = i


def two_sum_2(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]


def dir_reduc(arr):
    opposite = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    stack = []
    for direction in arr:
        if stack and stack[-1] == opposite[direction]:
            stack.pop()
        else:
            stack.append(direction)
    return stack


def sum_of_differences(arr):
    return 0 if len(arr) <= 1 else sum(
        sorted(arr, reverse=True)[i] - sorted(arr, reverse=True)[i + 1] for i in range(len(arr) - 1))


def sum_of_differences_2(arr):
    return max(arr) - min(arr) if arr else 0


class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        draft_after_crew = self.draft - (self.crew * 1.5)
        return draft_after_crew > 20


def if_chuck_says_so():
    return not True


def quadratic(x1, x2):
    return (1, -(x1 + x2), x1 * x2)


def integrate(coefficient, exponent):
    new_coefficient = coefficient // (exponent + 1)
    new_exponent = exponent + 1
    return f"{new_coefficient}x^{new_exponent}"


def integrate_2(coefficient, exponent):
    return f'{coefficient // (exponent + 1)}x^{exponent + 1}'


def goals(*args):
    return sum(args)


def goals_2(*a):
    return sum(a)


def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        principal += principal * interest * (1 - tax)
        years += 1
    return years


def who_is_paying(name):
    return [name] if len(name) <= 2 else [name, name[0:2]]


def whose_move(last_player, win):
    return 'white' if last_player == 'black' and win == False else (
        'white' if last_player == 'white' and win == True else 'black')


def whoseMove_2(lastPlayer, win):
    return lastPlayer if win else 'white' if lastPlayer == 'black' else 'black'


def stringy(size):
    return ''.join(['1' if not i % 2 else '0' for i in range(size)])


def stringy_2(size):
    return ('10' * size)[:size]


def triple_trouble(str1, str2, str3):
    return ''.join([str1[i] + str2[i] + str3[i] for i in range(len(str1))])


def triple_trouble_2(one, two, three):
    return ''.join(''.join(a) for a in zip(one, two, three))


def validate_hello(greetings):
    words = {"hello": "english", "ciao": "italian", "salut": "french", "hallo": "german", "hola": "spanish",
             "ahoj": "czech republic", "czesc": "polish"}
    return any(word in greetings.lower() for word in words)


def validate_hello_2(greetings):
    return any(x in greetings.lower() for x in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc'])


def symmetric_point(p, q):
    return [2 * q[0] - p[0], 2 * q[1] - p[1]]


def is_palindrome(s):
    return s.lower() == s.lower()[::-1]


def count(s):
    return {char: s.count(char) for char in s}


def six_toast(num):
    return abs(num - 6)


from math import factorial


def am_i_wilson(n):
    return False if n <= 1 else (factorial(n - 1) + 1) % (n * n) == 0


factorial_cache = {}


def factorial_cached(n):
    if n in factorial_cache:
        return factorial_cache[n]
    result = factorial(n)
    factorial_cache[n] = result
    return result


def am_i_wilson_2(P):
    if P <= 1:
        return False
    return (factorial_cached(P - 1) + 1) % (P * P) == 0


from math import ceil


def aspect_ratio(x: int, y: int):
    return ceil(y * (16 / 9)), y


def lowercase_count(strng):
    return sum(1 for letter in strng if letter.islower())


def lowercase_count_2(strng):
    return sum(a.islower() for a in strng)


def draw_stairs(n):
    for i in range(n):
        print(" " * i + "I")


def draw_stairs_2(n):
    return '\n'.join(' ' * i + 'I' for i in range(n))


def derive(coefficient, exponent):
    return f'{coefficient * exponent}x^{exponent - 1}'


def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    if 14 <= age < 18:
        return "drink coke"
    if 18 <= age < 21:
        return "drink beer"
    else:
        return "drink whisky"


def people_with_age_drink_2(age):
    if age > 20: return 'drink whisky'
    if age > 17: return 'drink beer'
    if age > 13: return 'drink coke'
    return 'drink toddy'


def build_string(*args):
    return "I like {}!".format(", ".join(args))


def any_arrows(arrows):
    for arrow in arrows:
        if 'damaged' not in arrow or not arrow['damaged']:
            return True
    return False


def any_arrows_2(arrows):
    return any('damaged' not in arrow or not arrow['damaged'] for arrow in arrows)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f'{self.name}s age is {self.age}'


class Solution:
    @staticmethod
    def main(*args):
        print("Hello World!")


class Solution_2:
    def main(self):
        print('Hello World!')


import random


class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


def filter_list(l):
    return [item for item in l if isinstance(item, int)]


import random

log = []


def roll_dice():
    log.append("roll_dice")
    return random.randint(1, 6)


def move():
    log.append("move")
    print("Moving...")


def combat():
    log.append("combat")
    print("Combat...")


def get_coins():
    log.append("get_coins")
    print("Getting coins...")


def buy_health():
    log.append("buy_health")
    print("Buying health...")


def print_status():
    log.append("print_status")
    print("Printing status...")


def do_turn():
    roll_result = roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()


def do_turn_2():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()


def do_turn_3():
    steps = [roll_dice, move, combat,
             get_coins, buy_health, print_status]

    for step in steps:
        step()


def move_1(position, roll):
    return (roll * 2) + position


def fake_bin(x):
    result = ''
    for num in x:
        if int(num) >= 5:
            result += '1'
        else:
            result += '0'
    return result


def fake_bin_2(x):
    return ''.join(['1' if int(digit) >= 5 else '0' for digit in x])


def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0


def get_volume_of_cuboid(length, width, height):
    return length * width * height


def get_ascii(str):
    return ord(str)


from datetime import datetime, timedelta


def period_is_late(last, today, cycle_length):
    days_passed = (today - last).days
    return days_passed > cycle_length


def mango(quantity, price):
    return (quantity - quantity // 3) * price


def pillars(num_pill, dist, width):
    return 0 if num_pill <= 1 else ((num_pill - 1) * dist * 100) + (num_pill - 2) * width


def pillars_2(num_pill, dist, width):
    return dist * 100 * (num_pill - 1) + width * (num_pill - 2) * (num_pill > 1)


def add_binary(a, b):
    return str(bin(a + b))[2:]


def add_binary_1(a, b):
    return format(a + b, 'b')


def first_non_consecutive(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] != arr[i] + 1:
            return arr[i + 1]


def check_alive(health):
    return False if health <= 0 else True


def check_alive_2(health):
    return health > 0


def two_sort(array):
    return '***'.join(sorted(array)[0])


def two_sort_2(lst):
    return '***'.join(min(lst))


def duty_free(price, discount, holiday_cost):
    return holiday_cost // (price * discount / 100)


def two_highest(arg1):
    if not arg1:
        return []
    elif len(arg1) == 1:
        return arg1
    new_list = [max(arg1), max([x for x in arg1 if x < max(arg1)])]
    return new_list if new_list[0] != new_list[1] else max(arg1)


def two_highest_2(arg1):
    return sorted(set(arg1), reverse=True)[:2]


def chromosome_check(chromosome):
    return "Congratulations! You're going to have a son." if 'Y' in chromosome else "Congratulations! You're going to have a daughter."


def is_even(n):
    return False if n % 2 or isinstance(n, float) else True


def is_even_2(n):
    return not n % 2 and not isinstance(n, float)


def is_even_3(n):
    return not n % 2


def billboard(name, price=30):
    cost = 0
    for _ in range(len(name)):
        cost += price
    return cost


def distinct(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]


def find_short(s):
    return min(len(item) for item in s.split())


def find_shortest_word(text):
    return min((len(item), item) for item in text.split())[1]


def delete_nth(order, max_e):
    result = []
    counts = {}
    for num in order:
        if num not in counts:
            counts[num] = 0
        if counts[num] < max_e:
            result.append(num)
            counts[num] += 1
    return result


def array(s):
    return None if not s or len(s.split(',')) <= 2 else ' '.join(num for num in s.split(',')[1:-1])


def array_2(strng):
    return ' '.join(strng.split(',')[1:-1]) or None


def is_opposite(s1, s2):
    return False if not s1 and not s2 else s1.swapcase() == s2


def is_opposite_2(s1, s2):
    return False if not (s1 or s2) else s1.swapcase() == s2


def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    north_south = 0
    east_west = 0

    for direction in walk:
        if direction == 'n':
            north_south += 1
        elif direction == 's':
            north_south -= 1
        elif direction == 'e':
            east_west += 1
        elif direction == 'w':
            east_west -= 1

    return north_south == 0 and east_west == 0


def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


def isValidWalk_2(walk):
    if (walk.count('n') == walk.count('s') and
            walk.count('e') == walk.count('w') and
            len(walk) == 10):
        return True
    return False


def print_array(arr):
    return ",".join([str(item) for item in arr])


def greet_5(name):
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"


def solution(a, b):
    return a + b + a if len(a) < len(b) else b + a + b


def friend(x):
    return [name for name in x if len(name) == 4]


def job_matching(candidate, job):
    return candidate['min_salary'] <= job['max_salary'] or (candidate['min_salary'] - 0.1 * candidate['min_salary']) <= \
        job['max_salary']


def match(candidate, job):
    return candidate['min_salary'] * 0.9 <= job['max_salary']


def solution_5(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    return ((given_mass1 / molar_mass1 + given_mass2 / molar_mass2) * (temp + 273.15) * 0.082) / volume


def split_and_merge(string_, separator):
    return " ".join(separator.join(word) for word in string_.split(" "))


import re


def increment_string(s):
    match = re.search(r'(\d+)$', s)

    if match:
        num = match.group()
        num_len = len(num)
        new_num = str(int(num) + 1)
        new_num = new_num.zfill(num_len)
        return s[:match.start()] + new_num
    else:
        return s + '1'


def cookie(x):
    return f'Who ate the last cookie? It was {"Zach" if type(x) is str else "Monica" if type(x) in [int, float] else "the dog"}!'


def no_boring_zeros(n):
    return 0 if not n else int(str(n).rstrip('0'))


def no_boring_zeros_2(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0


def area_or_perimeter(l, w):
    return l * w if l == w else 2 * l + 2 * w


def area_or_perimeter_2(l, w):
    return l * w if l == w else (l + w) * 2


def enough(cap, on, wait):
    return 0 if cap - on >= wait else abs(cap - (on + wait))


def enough_2(cap, on, wait):
    return max(0, wait - (cap - on))


def position(alphabet):
    alphabet_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }

    return f'Position of alphabet: {alphabet_dict.get(alphabet)}'


def get_char(c):
    return chr(c)


def find_average(numbers):
    return 0 if not numbers else sum(numbers) / len(numbers)


def high(x):
    alphabet_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }

    return sum([alphabet_dict[letter] for letter in x if letter in alphabet_dict])


def high_2(x):
    alphabet_dict = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }

    max_score = 0
    highest_word = ''

    words = x.split()
    for word in words:
        score = sum(alphabet_dict[letter] for letter in word)
        if score > max_score:
            max_score = score
            highest_word = word

    return highest_word


def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - (col - 1)) * (tot_rows - row)


def final_grade(exam, projects):
    if exam > 90 or projects > 10: return 100
    if exam > 75 and projects >= 5: return 90
    if exam > 50 and projects >= 2: return 75
    return 0


def problem(a):
    return "Error" if isinstance(a, str) else (a * 50) + 6


def problem_2(a):
    try:
        return a * 50 + 6
    except TypeError:
        return "Error"


def xor(a, b):
    return (a and not b) or (not a and b)


def xor_2(a, b):
    return a != b


def plural(n):
    return n != 1


def get_real_floor(n):
    if 0 < n < 13:
        return n - 1
    elif n <= 0:
        return n
    else:
        return n - 2


def get_real_floor_2(n):
    if n <= 0: return n
    if n < 13: return n - 1
    if n > 13: return n - 2


def multiple_of_index(arr):
    return [arr[i] for i in range(len(arr)) if i == 0 or (i != 0 and arr[i] % i == 0)] if arr[0] == 0 else [arr[i] for i
                                                                                                            in range(1,
                                                                                                                     len(arr))
                                                                                                            if arr[
                                                                                                                i] % i == 0]


def multiple_of_index_2(arr):
    return [j for i, j in enumerate(arr) if (j == 0 and i == 0) or (i != 0 and j % i == 0)]
