from Programmer import *


def employee_print():
    print("Employee Details:")
    soft.print()


def programmer_levele():
    soft.levele()


def programmer_annual_salary():
    print("Employee annual salari: ", end="")
    print(f'{soft.annual_salary():.2f}$')


soft = None
soft_f_name = ""
soft_l_name = ""
soft_main = ""
soft_second = ""
soft_age = int
soft_salary = float
soft_level = int

while True:
    print("--Main Menu--")
    print("1. Create new Employee")
    print("2. Show Employee details")
    print("3. Show Employee annual salary")
    print("4. Show Employee level")
    print("0. Exit Program")
    wee = int(input("Please select the first option : "))
    if wee == 0:
        print("Successful End!")
        break
    elif wee == 1:
        soft_f_name = input("Enter Employee First name: ")
        soft_l_name = input("Enter Employee Last name: ")
        soft_main = input("Main Programing language: ")
        soft_second = input("Second Programing language: ")
        soft_age = int(input("Enter Employee Ages: "))
        soft_salary = float(input("Enter Employee Salary: "))
        soft_level = int(input("Enter level: "))
        soft = Programmer(soft_f_name, soft_l_name, soft_main, soft_second, soft_age, soft_salary, soft_level)
        continue
    elif wee == 2:
        employee_print()
        continue
    elif wee == 3:
        programmer_annual_salary()
        continue
    elif wee == 4:
        programmer_levele()