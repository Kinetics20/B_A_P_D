# 01
def shorten(any_str):
    return ''.join([word[0] for word in any_str.split()]).upper()


# print(shorten('where is my home ? I think there you are'))

# 02
def name_sorter(any_name_list):
    my_dict = {'male': [], 'female': []}
    for word in sorted(any_name_list):
        if word[-1] == 'a':
            my_dict['female'].append(word)
        else:
            my_dict['male'].append(word)
    return my_dict


all_names = ['Adam', 'Bartosz', 'Cezary', 'Dariusz', 'Anna', 'Barbara', 'Celina', 'Dorota']
# print(name_sorter(all_names))
new_list_d_2 = [3, 90, 5, 6, 8, 20, 60]


def create_dict_from_list(any_list_1, any_list_2):
    new_dict = dict(zip(any_list_1[:6], any_list_2[:6:]))
    return new_dict


# print(create_dict_from_list(new_list_d_2, all_names))

def create_list_from_dict_for_key(any_dict):
    return list(any_dict), list(any_dict.values()), list(any_dict.items())


# print(create_list_from_dict_for_key({3: 'Adam', 90: 'Bartosz', 5: 'Cezary', 6: 'Dariusz', 8: 'Anna', 20: 'Barbara'}))


# 03

def check_palindrome(any_str):
    try:
        new_any_str = any_str.lower().replace(' ', '')
        return True if new_any_str == new_any_str[::-1] else False
    except AttributeError:
        return 'There is not a string ! '


# print(check_palindrome(' '))

def div(a, b):
    return [numbers for numbers in range(a, b + 1) if not numbers % 2 and numbers % 3]


print(div(-6, 20))
