# lang = ('Python','C#','PHP','Java','TypeScript')
# print(len(lang))
# print(type(lang))
# print(lang)
# lang[4] = "C++"
# print(lang[5])


# fruits =("Apple","Banana","Orange","Cherry")
# print(f"Type: {type(fruits)}\nLenght: {len(fruits)}")
# # fruits[0] = "Banana" #Error
# print("Banana"in fruits)

# del fruits

# fruits ={"Apple","Banana","Orange","Cherry"}
# print(f"Type: {type(fruits)}\nLenght: {len(fruits)}\nData: {fruits}")
# print('Banana'in fruits)
# fruits.add ('Lemon')
# print(f"Type: {type(fruits)}\nLenght: {len(fruits)}\nData: {fruits}")


# Користувач вводить із клавіатури рядок. 
# Зробіть поворот рядків і отриманий результат виведіть на екран.

# choise = (input("Enter choise: "))
# print(choise[::-1])


#__________2_________
# Користувач вводить із клавіатури рядок і символ для пошуку. 
# Порахуйте скільки разів у рядку зустрічається шуканий символ. 
# Отримане число виведіть на екран.

# s = "ABADACB"
# n = s.count('A')
# print(n)    # 3



#_____4_______
#У вас є два кортежі. Створіть третій кортеж, 
# який є об'єднанням перших двох кортежів.

# list1 =("1","2","3")
# list2=("4","5","6")5+
# sum=list1.__add__(list2)
# print(sum)

#__________5________
# У вас є список елементів. 
# Напишіть програму, щоб створити новий список, 
# який містить тільки унікальні елементи зі старого списку.

import random
# arr=[]
# for i in range(7):
#     arr.append(random.randint(1,10))
# print(arr)
# set={0,}
# set.clear()
# for i in range(7):
#     set.add(arr[i])
# print(set)


#_____________6____________-
# У вас є дві множини. Напишіть програму, 
# щоб знайти елементи, які є спільними для обох множин.
# set1={1,3,5,7}
# set2={4,6,8,3,5}
# # sumSet=set1.intersection(set2)
# # print(sumSet)
# result=[]

# for element in set1:
#     if element in set2:
#         result.append(element)

# print(result)

#_____________7________
# У вас є список чисел. 
# Напишіть програму, щоб відсортувати цей список 
# в порядку зростання без використання вбудованих функцій сортування.

arr=[]
for i in range(10):
    arr.append(random.randint(1,10))
print(arr)

j=1
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[j]>arr[i]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)

