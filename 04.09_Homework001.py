# Задание 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

numberOfDay = int(input('Введите цифру дня недели '))
week = [1, 2, 3, 4, 5, 6, 7]
def DayX(num):
    if num in week:
        return True
    else:
        return False
print(DayX(numberOfDay))