import random


# Користувач вводить із клавіатури два числа.
# Залежно від вибору користувача потрібно показати суму двох чисел,
# різницю двох чисел, середньоарифметичне або добуток двох чисел.

# number1 = int(input("Enter number 1:"))
# number2 = int(input("Enter number 2:"))
# choise = (input("Enter choise: \n-\n+\n*\n/\n"))
# # number = random.randint(1, 1)
# # print(f"{number} {type(number)}")
# if choise == "-":
#     print(number1-number2)
# elif choise == "+":
#     print(number1+number2)
# elif choise == "*":
#     print(number1*number2)
# elif choise == "/":
#     print(number1/number2)
# else:
#     print("Wrong choise!")




number1 = int(input("Enter number 1:"))
number2 = int(input("Enter number 1:"))


if number1>number2:
    print(number1)
elif number1<number2:
    print(number2)