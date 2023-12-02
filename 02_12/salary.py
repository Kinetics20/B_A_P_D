class Employee:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def set_salary(self, salary):
        if isinstance(salary, (int, float)) and salary >= 0:
            self._salary = salary
        else:
            print('Niewłaściwa wartość')


test = Employee(1, 'Paweł', 'Lis')
test.set_salary(2500.90)
print(test._salary)
