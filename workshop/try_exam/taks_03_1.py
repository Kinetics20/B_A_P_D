def check_palindrome(any_txt):
    new_txt = any_txt.lower().replace(' ', '')
    return new_txt == new_txt[::-1]


if __name__ == '__main__':
    print(check_palindrome('Kobyła ma mały bok'))
    print(check_palindrome('Sth about THE future'))

