# 01

def shorten(any_str):
    return "".join([word[0] for word in any_str.split()]).upper()


# if __name__ == '__main__':
#     print(shorten('Ala ma kota and kot ma Ale'))

def name_sorter(any_list):
    new_dict = {'male':[], 'female':[]}
    for word in sorted(any_list):
        if word[-1] == 'a':
            new_dict['female'].append(word)
        else:
            new_dict['male'].append(word)
    return new_dict
