class Calculator:
    def __init__(self):
        self.new_list = []

    def add(self, num1, num2):
        result = num1 + num2
        operation = f'added {num1} to {num2} got {result}'
        self.new_list.append(operation)
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        operation = f'multiplied {num1} with {num2} got {result}'
        self.new_list.append(operation)
        return result

    def print_operations(self):
        for operation in self.new_list:
            print(operation)


calc = Calculator()
res_odd = calc.add(5, 3)
res_multiply = calc.multiply(40, 2)

print('Addition result : ', res_odd)
print('Multiplication result : ', res_multiply)

print('\nHistory of operations : ')
calc.print_operations()
