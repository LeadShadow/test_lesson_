# Завдання: Порівняння чисел
# Напишіть програму на Python, яка порівнює два числа, введені користувачем, і виводить більше з них.
#
# Запитайте користувача про перше число.
# Запитайте користувача про друге число.
# Використайте умовний оператор, щоб порівняти ці числа.
# Виведіть більше з чисел.
# Приклад виконання програми:

num1 = int(input('введи перше число: '))
num2 = int(input('введи друге число: '))
if num1 > num2:
    print('num1 > num2')
elif num1 < num2:
    print('num2 > num1')
