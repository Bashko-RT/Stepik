# Для каждого введённого числа проверить:
# если число меньше 10, то пропускаем это число;
# если число больше 100, то прекращаем считывать числа;
# в остальных случаях вывести это число обратно на консоль в отдельной строке.
# x = (int(input()))
# while 10 > x:
#     if x > 99:
#         print(x)
#         break


# Напишите программу, которая распечатает все натуральные числа кратные 5 от 195 до 6785 включительно в порядке убывания.
# x = 6785
# while x >= 195:
#     print(x)
#     x -= 5

# Мишка Лимак хочет стать самым большим медведем, ну, или хотя бы стать больше своего старшего брата Боба.
# Сейчас вес Лимака равен a, а вес Боба равен b. Гарантируется, что вес Лимака меньше или равен весу Боба.
# Лимак ест много, и его вес утраивается каждый год, а вес Боба удваивается каждый год.
# Через сколько целых лет Лимак станет строго больше (т. е. будет весить строго больше) Боба?
# Входные данные
# В единственной строке находятся два целых числа a и b (1 <= a <= b <= 10) — веса Лимака и Боба соответственно.

# a, b = map(int, input().split())
# year = 0
# while a <= b:
#     a = a * 3
#     b = b * 2
#     year += 1
# print(year)

# Убрать цифру 4 из списка.
# numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6, 6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9, 2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4, 8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5, 6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2, 4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]
# while 4 in numbers:
#     numbers.remove(4)
# print(*numbers)

# На вход программе поступает слово. Вам необходимо воспроизвести процесс, в котором каждый раз у этого слово будет пропадать первая и последняя буква.
# Этот процесс необходимо закончить, когда в слове останется только одна буква или слово  станет пустой строкой.
# При этом результат каждого этапа нужно выводить
# s = input("")
# while len(s) > 0:
#     print(s)
#     s = s[1:-1]

# Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке,
# и после первого введенного нуля выводит сумму полученных на вход чисел.
# x = int(input())
# y = 0
# while x != 0:
#     y += x
#     x = int(input())
# print(y)

# Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
# Для каждого введённого числа проверить:
# если число меньше 10, то пропускаем это число;
# если число больше 100, то прекращаем считывать числа;
# в остальных случаях вывести это число обратно на консоль в отдельной строке.
# while True:
#     x = int(input())
#     if x < 10:
#         continue
#     elif x > 100:
#         break
#     else:
#         print(x)

# name = "Salavat"
#
# count = 1
# while count <= 5:
#     print(f"{name}, count = {count} ")
#     count += 1


# text = input()
# while text != "exit":
#     print(text)
#     text = input()


while True:
    name = input()
    if name == "exit":
        break
    else:
        print(name)
