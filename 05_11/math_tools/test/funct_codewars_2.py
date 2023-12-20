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




