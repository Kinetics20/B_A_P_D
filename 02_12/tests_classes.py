# 01
import math


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


# Abstraction 02

class SequenceOfNumbers:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __len__(self):
        return math.ceil((self.stop - self.start) / self.step)

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError('Index too big')
        if index < 0:
            raise IndexError('Index must be higher than zero')
        return self.start + index * self.step


def middle_elements(list_of_list):
    output = []
    for inner_list in list_of_list:
        length = len(inner_list)
        if length == 0:
            continue
        middle_index = length // 2
        output.append(inner_list[middle_index])
    return output


# Abstraction 04

class SingleChoiceQuestion:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def ask(self):
        print(self.question)
        valid_answers = []
        for i, answer in enumerate(self.answers):
            answer_letter = chr(i + 97)
            valid_answers.append(answer_letter)
            print(f'{answer_letter}) {answer}')
        while True:
            answer = input('Answer :')
            if answer in valid_answers:
                print()
                return answer
            else:
                print('Invalid answer , try again')


class Questionnaire:
    def __init__(self, tittle):
        self.tittle = tittle
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        print(self.tittle)
        print()
        answers = {}
        for i, question in enumerate(self.questions):
            answers[i] = question.ask()
        print('Thank you')
        return answers


questionnaire = Questionnaire('Ankieta dotycząca zadowolenia z wyboru laptopa')
q1 = SingleChoiceQuestion('Matryca', ['mniej niż 15 cali', 'od 15 do 17 cali', 'więcej niż 17 cali'])
q2 = SingleChoiceQuestion('Rodzaj ekranu', ['matowy', 'błyszczący'])
q3 = SingleChoiceQuestion('Czy polecisz go znajomemu?',
                          ['zdecydowanie tak', 'raczej tak', 'nie mam zdania', 'raczej nie',
                           'zdecydowanie nie'])
questionnaire.add_question(q1)
questionnaire.add_question(q2)
questionnaire.add_question(q3)
answers = questionnaire.run()
print(answers)


# Inheritance Cart 01

class Cart:
    def __init__(self):
        self.products = []

    def add(self, price, name):
        self.products.append((price, name))

    def summary(self):
        return self.products


class Discount20PercentCart(Cart):

    def summery(self):
        return [(price * 0.8, name) for price, name in self.products]


class Above3ProductsCheapestFreeCart(Cart):
    def summery(self):
        if len(self.products) <= 3:
            return self.products
            # products_copy = self.products.copy()

        products_copy = sorted(self.products)
        cheapest_product = products_copy[0]
        cheapest_product_name = cheapest_product[1]
        products_copy[0] = (0, cheapest_product_name)
        return products_copy


# decorator @property

class Circle:

    def __init__(self, radius):
        self._radius = radius
        self.area = math.pi * radius ** 2
        self.circumference = 2 * math.pi * radius

    def get_radius(self):
        return self._radius

    @property
    def radius(self):
        return self.get_radius()

    @radius.setter
    def radius(self, new_radius):
        self._radius = new_radius
        self.area = math.pi * new_radius ** 2
        self.circumference = 2 * math.pi * new_radius


class Square:
    def __init__(self, side):
        self.set_side(side)

    def get_side(self):
        return self._side

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def get_diagonal(self):
        return self._diagonal

    def set_side(self, new_side):
        self._side = new_side
        self._perimeter = new_side * 4
        self._area = new_side ** 2
        self._diagonal = (new_side ** 2 + new_side ** 2) ** 0.5

    def set_perimeter(self, new_perimeter):
        self.set_side(new_perimeter / 4)
        # self._perimeter = new_perimeter
        # self._side = new_perimeter / 4
        # self._diagonal = (self._side ** 2 + self._side ** 2) ** 0.5
        # self._area = self._side ** 2

    def set_diagonal(self, new_diagonal):
        self.set_side(((new_diagonal ** 2) / 2) ** 0.5)
        # self._diagonal = new_diagonal
        # self._side = ((new_diagonal ** 2) / 2) ** 0.5
        # self._area = self._side ** 2
        # self._perimeter = self._side * 4

    def set_area(self, new_area):
        self.set_side(new_area ** 0.5)
        # self._area = new_area
        # self._side = new_area ** 0.5
        # self._diagonal = (self._side ** 2 + self._side ** 2) ** 0.5
        # self._perimeter = self._side * 4


test = Square(2)
print(test.set_area(9))
