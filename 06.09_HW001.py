# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# #Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11

number = str(input("Введите свое вещественное число: "))
    
def Sum_Of_Numbers(num):
    sum = 0
    for i in num:
        if i != '.':
            sum += int(i)
    return sum

print(Sum_Of_Numbers(number))