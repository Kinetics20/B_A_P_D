from random import randint

possible_dices = ('D100', 'D20', 'D12', 'D10', 'D8', 'D6', 'D4', 'D3')


def roll_the_dice(dice_code):
    for dice in possible_dices:
        if dice in dice_code:
            try:
                # result = dice_code.split(dice)
                # multiply = result[0]
                # modifier = result[1]
                (multiply, modifier) = dice_code.split(dice)
            except ValueError:
                return 'Wrong Input'
            dice_value = int(dice[1:])
            break
    else:
        return 'Wrong Input'
    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return 'Wrong Input'
    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return 'Wrong Input'
    return sum([randint(1, dice_value) for _ in range(multiply)]) + modifier


if __name__ == '__main__':
    print(roll_the_dice("2D10+10"))
    print(roll_the_dice("D6"))
    print(roll_the_dice("2D3"))
    print(roll_the_dice("D12-1"))
    print(roll_the_dice("DD34"))
    print(roll_the_dice("4-3D6"))
