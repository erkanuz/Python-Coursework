from employeer import *


class Programmer(Employeer):

    def __init__(self, f_name, l_name, language_main, language_second, age, salary, level):
        super().__init__(f_name, l_name, language_main, language_second, age)
        self.salary = salary
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.level = level
        self.language = Language(language_main, language_second)

    def annual_salary(self):
        return self.salary * 12

    def levele(self):
        if self.level == 2:
            print(self.f_name + " : You are Junior!")
        else:
            print(self.f_name + " : You are Senior!")

    def print(self):
        print(
            f'Your name is: {self.full_name()} || Age: {self.age}\n'
            f'Programing language: {self.get_language()}\n'
            f'Salary: {self.salary:.2f}$'
        )