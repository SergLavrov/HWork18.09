
# Задача 1.
# Вы занимаетесь сборкой игрушечных машинок. Каждая машинка должна иметь четыре колеса,
# один корпус и две фигурки человечков внутри.
# Напишите функцию, которая будет принимать количество колес, корпусов и человечков
# и возвращать количество машинок, которые можно собрать из этих деталей.
#
# Примеры:
# cars(2, 48, 76) ➞ 0
# # 2 колеса, 48 корпусов, 76 человечков
# cars(43, 15, 87) ➞ 10
# cars(88, 37, 17) ➞ 8

def qual_cars(wheels, car_bodies, people):

    if wheels < 4 or car_bodies < 1 or people < 2:
        return ('The number of cars is zero')

    print(f'{wheels} wheels, {car_bodies} car_bodies, {people} people')

    cars = wheels // 4

    if people // 2 < wheels // 4:
        cars = people // 2

    return (f'Number of cars {cars}')

wheels1 = int(input('Enter quality of wheels: '))
car_bodies1 = int(input('Enter quality of car_bodies: '))
people1 = int(input('Enter people: '))

result = qual_cars(wheels1, car_bodies1, people1)
print(result)



# Задача 2
# Медиана набора чисел — это число, которое находится в середине этого набора,
# если его упорядочить по возрастанию. То есть такое число, что половина из элементов набора
# не меньше него, а другая половина не больше.
#
# Напишите функцию, которая будет принимать отсортированный список чисел и возвращать медиану.
# Если число дробное, его нужно округлить до десятых.
#
# Примеры:
# median([1, 2, 4, 5, 6, 8, 8, 8, 10]) ➞ 6
# median([2, 2, 6, 8, 8, 10, 10]) ➞ 8
# median([1, 2, 2, 4, 7, 8, 9, 10]) ➞ 5.5

import random

def median(someList):

    if len(someList) % 2 != 0:
        number = someList[int(len(someList) / 2)]
        return number
    else:
        num1 = someList[int(len(someList) / 2)]
        num2 = someList[int(len(someList) / 2) - 1]

        number = round((num1 + num2) / 2, 1)
        return number


n = int(input())
someList1 = []
for i in range(n):
    someList1.append(random.randint(1, 25))
print(someList1)

sortedList = sorted(someList1)
print(sortedList)

result = median(sortedList)
print(result)


