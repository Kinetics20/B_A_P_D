def div(a, b):
    return [num for num in range(a, b + 1) if not num % 2 and num % 3]


if __name__ == '__main__':
    print(div(0, 20))
