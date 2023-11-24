from random import randint


def roll(dices, dice_type=6, modifier=0):
    if dice_type not in (3, 4, 6, 8, 10, 12, 100):
        raise Exception('No such dice')
    return sum(randint(1, dice_type) for _ in range(dices)) + modifier


if __name__ == '__main__':
    print(roll(3, 8, -2))


def roll_2(dices, dice_type=6, modifier=0):
    if dice_type not in (3, 4, 6, 8, 10, 12, 100):
        raise Exception('No such dice')
    counter = 0
    for _ in range(dices):
        counter += randint(1, dice_type)

    total = counter + modifier
    return total


if __name__ == '__main__':
    print(roll_2(3, 8, -2))
