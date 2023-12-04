# 01
class User:
    def __init__(self, ):
        self.history = []

    def addition(self, num_1, num_2):
        rest = num_1 + num_2
        self.history.append(rest)
        return f'added {num_1} to {num_2} got {rest}'

    def subst(self, num_1, num_2):
        rest = num_1 - num_2
        self.history.append(rest)
        return f'subst {num_1} from {num_2} got {rest}'

    def divide(self, num_1, num_2):
        rest = num_1 // num_2
        self.history.append(rest)
        return f'divided  {num_1} by {num_2} got {rest}'

    def print_operation(self):
        for i, item in enumerate(self.history):
            print(f' {i} , {item}')


u1 = User()
u2 = User()
u3 = User()


# print(u1.addition(5, 10))
# print(u2.addition(565, 1010))
# print(u3.addition(50, 105658))
#
# print(u1.subst(5, 10))
# print(u2.subst(565, 1010))
# print(u3.subst(58954, 15650))
#
# print(u1.divide(5, 10))
# print(u2.divide(565, 1010))
# print(u3.divide(58954, 15650))
#
# print()
# print('Calc_1')
# u1.print_operation()
# print()
# print('Calc_2')
# u2.print_operation()
# print()
# print('Calc_3')
# u3.print_operation()

# 02

class Shape:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f'figure about color {self.color} and the center in the point {self.x, self.y}'

    def describe(self):
        # return str(self)
        return self.__str__()
    # self.__str__() to jest to samo co str(self)
    def distance(self, shape):
        return ((self.x - shape.x) ** 2 + (self.y - shape.y) ** 2) ** 0.5


s1 = Shape(10, 25, 'white')
s2 = Shape(-25, 30, 'Green')


# print(f'distance between:\n{s1}\nand\n{s2}\nis : {s1.distance(s2)}')
# print(s1.describe())
# print(s2.describe())

# 03

class BankAccount:

    def __init__(self, number):
        self.number = number
        self.cash = 0

    def print_info(self):
        return f'number account : {self.number} balance account : {self.cash}'

    def deposit_cash(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            return
        self.cash += amount
        return self.cash

    def withdraw_cash(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            return
        if amount > self.cash:
            amount = self.cash
        self.cash -= amount
        return amount


# account = BankAccount('0121541254')
# print(account.print_info())
# print(account.deposit_cash(100))
# print(account.print_info())
# print(account.deposit_cash(1000))
# print(account.print_info())
# print(account.deposit_cash(100))
# print('get 700', account.withdraw_cash(700))
# print(account.print_info())
# print('get 800', account.withdraw_cash(800))
# print(account.print_info())

# 04

class Employee:

    def __init__(self, id, f_name, l_name):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name

    def __str__(self):
        return f'employee parameters -> id :{self.id} , name :{self.f_name} , sure_name: {self.l_name}'

    def info_employee(self):
        return str(self)

    def set_salary(self, salary):
        if isinstance(salary, (int, float)) and salary > 0:
            self._salary = salary
            print(salary)
        else:
            print(f'invalid value of salary')


worker_1 = Employee(254, 'John', 'Smith')
print(worker_1.info_employee())
worker_1.set_salary(250)
