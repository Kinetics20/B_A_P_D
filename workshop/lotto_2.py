from random import shuffle


def lotto_():
    liczby = list(range(1, 49 + 1))
    shuffle(liczby)
    # draft_numbers = ", ".join([str(liczba) for liczba in liczby[:6]])
    draft_numbers = [liczba for liczba in liczby[:6]]
    # sorted(draft_numbers)
    return sorted(draft_numbers)


# print(lotto_())

# LOTTO_simulator

def get_num():
    while True:
        try:
            score = int(input('Choose the number: '))
            break
        except ValueError:
            print('It is not a number , try again ')

    return score


def get_nums():
    score = []
    while len(score) < 6:
        number = get_num()
        if number not in score and 0 < number <= 49:
            score.append(number)

    return score


# print(get_nums())

def print_numbers(numbers):
    # new_l = [str(number) for number in sorted(numbers)]
    # print(", ".join(new_l))
    print(', '.join(str(number) for number in sorted(numbers)))


# print_numbers([1, 2, 3, 4, 7, 5])

def drawing_numbers():
    numbers = list(range(1, 50))
    shuffle(numbers)
    return numbers[:6]


# print(drawing_numbers())

def lotto():
    user_numbers = get_nums()
    print('Yor numbers: ')
    print_numbers(user_numbers)

    random_numbers = drawing_numbers()
    print('Lotto numbers: ')
    print_numbers(random_numbers)

    hits = 0
    for number in user_numbers:
        if number in random_numbers:
            hits += 1

    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")


if __name__ == '__main__':
    lotto()
