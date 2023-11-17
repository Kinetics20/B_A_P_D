#!/usr/bin/python3

def check_palindrome(word):
    return True if word == word[::-1] else False


print(check_palindrome('ala'))


def check_palindrome_2(chain_str):
    temp = chain_str.split()
    for index in temp:
        if index == index[::-1]:
            return True
    return False


print(check_palindrome_2('ma kota ala'))
