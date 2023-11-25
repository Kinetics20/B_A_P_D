def user_input():
    possible_input = ['too small', 'too big', 'you won']
    while True:
        user_answer = input().lower()
        if user_answer in possible_input:
            break
        print("Input is not in ['too small', 'too big','you won']")
    return user_answer


def guess_the_number():
    print('Imagine number between 0 and 1000!')
    print('Press "Enter" to continue')
    input()
    min_num = 0
    max_num = 1000
    user_answer = ''
    while user_answer != 'you won':
        guess = (max_num - min_num) // 2 + min_num
        print(f'Your number is : {guess}')
        user_answer = user_input()
        if user_answer == 'too big':
            max_num = guess
        elif user_answer == 'too small':
            min_num = guess

    print('Gosh , at first time in my life ! I guess ! ')


if __name__ == '__main__':
    print(guess_the_number())
