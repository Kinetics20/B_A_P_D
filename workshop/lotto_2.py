from random import shuffle


def lotto():
    liczby = list(range(1, 49 + 1))
    shuffle(liczby)
    # draft_numbers = ", ".join([str(liczba) for liczba in liczby[:6]])
    draft_numbers = [liczba for liczba in liczby[:6]]
    # sorted(draft_numbers)
    return sorted(draft_numbers)


# print(lotto())

# def lotto_2():
#     while True:
#         num_1 = int(input('Choose a number: '))
#         num_2 = int(input('Choose a number: '))
#         num_3 = int(input('Choose a number: '))
#         num_4 = int(input('Choose a number: '))
#         num_5 = int(input('Choose a number: '))
#         num_6 = int(input('Choose a number: '))
#         if not num_1 in range(1, 50) or not num_2 in range(1, 50) or not num_3 in range(1, 50) or not num_4 in range(1,
#                                                                                                                      50) or not num_5 in range(
#                 1, 50) or not num_6 in range(1, 50):
#             print('some number you entered from out of range 1-49 , try again')
#             continue
#         if num_1 != num_2 != num_3 != num_4 != num_5 != num_6:
#             entered_numbers = [num_1, num_2, num_3, num_4, num_5, num_6]
#             nl = sorted(entered_numbers)
#             print(nl)
#             break

def get_num():
    while True:
        try:
            score = int(input('Choose the number: '))
            break
        except ValueError:
            print('It is not a number , try again ')

    return score


def get_nums():
    draft_numbers = []
    while len(draft_numbers) < 6:
        number = get_num()
        if number not in draft_numbers and 0 < number <= 49:
            draft_numbers.append(number)

    return draft_numbers


# print(get_nums())

def sorted_draft_numbers(numbers):
    new_l = [str(number) for number in sorted(numbers)]
    print(", ".join(new_l))

# sorted_draft_numbers(draft_numbers)
