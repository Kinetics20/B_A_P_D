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
