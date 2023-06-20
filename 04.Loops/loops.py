import random
people = ["John", "Adam", "Sara", "Paul", "eva"]
print(people)


# for person in people:
#     print(person)


# for person in people:
#     if person == "Sara":
#         print(person)


# count = 1
# while count <= 10:
#     print(f"Count: {count}")
#     count += 1


# Завдання 1

# Показати таблицю множення для числа,
# введеного користувачем. Наприклад,
# якщо користувач вводить число 7, потрібно показати:

# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# ...


# count = 1
# num = int(input("Enter number:"))
# while (count <= 10):
#     print(f"{num} * {count} = {num*count}")
#     count += 1



# value = 0
# sum = 0
# exit = False
# while not exit:
#     choise = int(input(f"Buy 36.57\tSale 37.45\n1.Buy\n2.Sale\n0.Exit\n"))
#     if choise == 1:
#         value = float(input("Enter value: "))
#         print(f"{value} dolars = {value*36.57} grn")
#     elif choise == 2:
#         value = float(input("Enter value: "))
#         print(f"{value} grn = {value/37.45} dolars")
#     elif choise == 0:
#         exit = True
#     else:
#         print("Wrong choise")



# Користувач вводить із клавіатури дві межі діапазону та число. Якщо число не потрапляє в діапазон,
# програма просить користувача повторно ввести число і так доти,
# доки він не введе число правильно.
# Програма відображає всі числа діапазону, виділяючи число знаками оклику.


# d1 = int(input("Enter range 1: "))
# d2 = int(input("Enter range 2: "))
# value = int(input("Enter Number: "))
# if d1 < value > d2:
#     value = int(input("Enter Number again: "))
# else:
#     print("+++++")




# Написати гру "Вгадай число". Програма загадує число в діапазоні від 1 до 500.
# Користувач намагається його вгадати.
# Після кожної спроби програма видає підказки: більше чи менше його число, ніж загадане.
# Наприкінці програма видає статистику: за скільки спроб вгадано число, скільки часу це зайняло.
# Передбачити вихід по 0 у разі, якщо користувачеві набридло вгадувати число.



numberRandom = random.randint(1, 10)
numUser = 0
exit = False
while not exit:
    numUser = int(input("Enter Number: "))
    if numUser == 0:
        exit = True
    elif numUser < numberRandom:
        print("number less")
    elif numUser > numberRandom:
        print("the number is bigger")
    elif numUser == numberRandom:
        print("you guessed it")
        exit = True