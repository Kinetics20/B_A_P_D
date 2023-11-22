def check_palindrome(any_txt):
    new_list = any_txt.split()
    for word in new_list:
        if word == word[::-1]:
            return True
        return False


if __name__ == '__main__':
    txt = 'ala ma kota'
    print(check_palindrome(txt))
