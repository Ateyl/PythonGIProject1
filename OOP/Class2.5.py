class Employee:

    #Class Variables
    raise_amount = 1.04

    def __init__(self, name, surname, salary):
        self.name=name
        self.surname=surname
        self.salary = salary
        self.email = f'{name.lower()}.{surname.lower()}@company.com'

    def fullname(self):
        return f'{self.name.title()} {self.surname.title()}'

    def raise_salary(self):
        self.salary *= self.raise_amount


    def __str__(self):
        return self.fullname()


    def __add__(self, other):
        return self.salary + other.salary

    print()
emp1 = Employee('Jack', 'Smith', 2000)
emp2 = Employee('Sarah', 'Gold', 3000)

print(emp1 + emp2)