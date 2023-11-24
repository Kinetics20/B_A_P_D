def name_sorter(any_list):
    new_dict = {'female': [], 'male': []}
    for word in sorted(any_list):
        if word[-1] == 'a':
            new_dict['female'].append(word)
        else:
            new_dict['male'].append(word)
    return new_dict


# input_list = ['Anna', 'Maria', 'Katarzyna', 'Jan', 'Andrzej', 'Piotr']
# print(name_sorter(input_list))

if __name__ == '__main__':
    input_list = ['Anna', 'Maria', 'Katarzyna', 'Jan', 'Andrzej', 'Piotr']
    print(name_sorter(input_list))
