# Метод для красивого вывода заголовков
import random


def title(title_string):
    print("\n" + title_string + "\n")


# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
# 6782 -> 23
# 0,56 -> 11


def task_1():
    title("Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.")
    number = input("Введите число: ")
    mySum = 0
    for i in range (len(number)):
        if number[i].isdigit():
            mySum += int(number[i])
    print(f"Сумма чисел введённого числа = {mySum}")


# Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def task_2():
    title("Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.")

    def factorial(number, answer = 1):
        while number >= 1:
            answer *= number
            number -= 1
        return answer
    n = int(input("Введите число N: "))
    array = []
    for i in range(1, n + 1):
        array.append(factorial(i))
    print(array)

# # Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# # округлённую до трёх знаков после точки.
# #
# # Пример:
# #
# # Для n = 6 -> 14.072


def task_3():
    title("Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,округлённую до трёх знаков после точки.")
    array = []
    n = int(input("Введите число n: "))
    answer = 0
    for i in range(1, n + 1):
        currentnumber = (1 + 1 / i) ** i
        answer += currentnumber
        array.append(currentnumber)
    print(round(answer, 3))


# # Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# # Найдите произведение элементов на позициях a и b.
# # Значения N, a и b вводит пользователь с клавиатуры.
def task_4():
    title("Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на позициях a и b.")
    n = int(input("Введите число N: "))
    array = []
    for i in range (-n, n + 1):
        array.append(i)

    position_1 = int(input("Введите позицию 1: "))
    position_2 = int(input("Введите позицию 2: "))
    answer = array[position_1 - 1] * array[position_2 - 1]
    print(f"Ответ: {answer}")

#
# # Задание 5 Реализуйте алгоритм перемешивания списка.


def task_5():
    def array_shuffle(array):
        length = len(array)
        for i in range (length):
            random_position = random.randrange(0, length)
            temp = array[i]
            array[i] = array[random_position]
            array[random_position] = temp
        return array

    testlist = [1, 2, 3, 4, 5, 6, 7]
    print(array_shuffle(testlist))


# task_1()
# task_2()
# task_3()
# task_4()
task_5()

