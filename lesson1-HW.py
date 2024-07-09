# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = 'as 23 fdfdg544'

# res = []
#
# for i in st:
#     if i.isdigit():
#         res.append(i)
#
# print(','.join(res))

# print(','.join(i for i in st if i.isdigit()))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'

# res = []
# x = ''
#
# for i in st:
#     if i.isdigit():
#         x += i
#     elif x.isdigit():
#         res.append(x)
#         x = ''
# if x.isdigit():
#     res.append(x)
#
# print(', '.join(res))

# print(', '.join(''.join(i if i.isdigit() else ' ' for i in st).split()))

# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# res = []
#
# for letter in greeting:
#     res.append(letter.upper())
#
# print(res)
# print([i.upper() for i in greeting])

#
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# res = []
#
# for i in range(50):
#     if i % 2 != 0:
#         res.append(i ** 2)
#
# print(res)
# print([i ** 2 for i in range(50) if i % 2 == 1])


#
# function
#
# - створити функцію яка виводить ліст

# def create_list(l):
#     for i in l:
#         print(i)
#
# create_list([1,2,3,4,5,6,7,8,9])

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def max_of_nums(a, b, c):
#     max_of_num = max(a, b, c)
#     print(max_of_num)
#     return max_of_num
#
# max_of_nums(1, 2, 3)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def min_max(*args):
#     max_of_num = max(args)
#     min_of_num = min(args)
#     print(max_of_num)
#     return min_of_num
#
# min_max(5, 10, 50, 6)

# - створити функцію яка повертає найбільше число з ліста

# def max_from_list(list):
#     return max(list)
#
# max_from_list(range(1,11))

# - створити функцію яка повертає найменьше число з ліста

# def min_from_list(list):
#     return min(list)
#
# min_from_list(range(1,11))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def sum_from_list(list):
#     return sum(list)
#
# sum_from_list(range(1,11))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def avg_from_list(list):
#     return sum(list) / len(list)
#
# avg_from_list(range(1,11))

# ################################################################################################
# 1)Дан list:
list1 = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число

def min_from_list():
    print(min(list1))

#   - видалити усі дублікати

def delete_all_duplicates():
    print(list(set(list1)))

#   - замінити кожне 4-те значення на 'X'

def change_to_X():

    # x = []
    # for i, value in enumerate(list1):
    #     if (i + 1) % 4 == 0:
    #         value = 'X'
    #         x.append(value)
    #     else:
    #         x.append(value)
    # print(x)

    print(['X' if (i + 1) % 4 == 0 else value for i, value in enumerate(list1)])


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')

# 3) вывести табличку множення за допомогою цикла while

def multitable():
    size = 9
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            res = i * j
            print(f'{res:3}', end='')
            j += 1
        i += 1
        print()

# 4) переробити це завдання під меню

while True:
    print('1) min_from_list')
    print('2) delete_all_duplicates')
    print('3) change_to_X')
    print('4) square')
    print('5) multitable')
    print('6) exit')

    choice = input('Your choice:')

    if choice == '1':
        min_from_list()
    elif choice == '2':
        delete_all_duplicates()
    elif choice == '3':
        change_to_X()
    elif choice == '4':
        square(5)
    elif choice == '5':
        multitable()
    elif choice == '6':
        break