import datetime
class Employee:

    #Class Variables
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, name, surname, salary):
        self.name=name
        self.surname=surname
        self.salary = salary
        self.email = f'{name.lower()}.{surname.lower()}@company.com'
        Employee.num_of_employees =+ 1

    def fullname(self):
        return f'{self.name.title()} {self.surname.title()}'

    def raise_salary(self):
        self.salary *= self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def emp_from_string(cls, string):
        name, surname, salary = string.split('-')
        return cls(name.titile(), surname.title(), float(salary))


    @staticmethod
    def is_workday(day):
        if day.weekday() in [5,6]:
            return False
        return True

emp1 = Employee('jack', 'Smith', 2000)
emp2 = Employee.emp_from_string('MARY-GOLD-3000')

emp1.raise_amount = 1.1

# print(Employee.is_workday())

print(Employee.raise_amount)
Employee.set_raise_amount(1.1)
print(Employee.raise_amount)

'MARY-GOLD-3000'


# print(emp1.salary)
# emp1.raise_salary()
# print(emp1.salary)
#
#
# print(emp1.num_of_employees)
# print(Employee.num_of_employees)

# print(emp1.surname)
# print(emp1.__dict__)
# print(Employee.__dict__)
#
# print(Employee.fullname(emp1))
# print(emp1.fullname())

# emp2 = Employee()

# print(emp1)
# print(emp2)
#
# print(emp1 == emp2)
# # print(type(Employee))
# emp1.name = 'Jack'
# print(emp1.name)