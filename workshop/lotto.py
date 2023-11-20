from random import shuffle


def lotek():
    empty_list = []
    for index in range(1, 50):
        empty_list.append(index)

    shuffle(empty_list)
    # return render_template(
    #     'lotto.html',
    #     l1=empty_list[0], l2=empty_list[1], l3=empty_list[2],
    #     l4=empty_list[3], l5=empty_list[4], l6=empty_list[5],
    # )

    # return str(empty_list[0:6])
    return ", ".join([str(liczba) for liczba in empty_list[:6]])


print(lotek())


def lotto():
    liczby = list(range(1, 49 + 1))
    shuffle(liczby)
    # liczby = liczby[:6]
    return ", ".join([str(liczba) for liczba in liczby[:6]])
