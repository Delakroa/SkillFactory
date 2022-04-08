'''
Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается
у пользователя любое число.

В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода
данных.
Далее программа работает по следующему алгоритму:

Преобразование введённой последовательности в список

Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)

Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или
равен этому числу.

При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле.
Реализуйте его также отдельной функцией.

Подсказка

Помните, что у вас есть числа, которые могут не соответствовать заданному условию.
В этом случае необходимо вывести соответствующее сообщение
'''


def sort_by_insert(list_input):
    list_int = list_input
    for i in range(1, len(list_int)):
        x = list_int[i]
        idx = i
        while idx > 0 and list_int[idx - 1] > x:
            list_int[idx] = list_int[idx - 1]
            idx -= 1
        list_int[idx] = x
    return list_int


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, right, middle + 1)


sequence_number_string = input("Введите последовательность чисел, через пробел: ")
element = int(input("Введите любое число из ранее введенных: "))

sequence_number_list = list(map(int, sequence_number_string.split(sep=" ")))

sequence_sorted = sort_by_insert(sequence_number_list)
print(f"Число по возрастанию (кол-во элементов): {sequence_sorted}")

element_index = binary_search(sequence_sorted, element, 0, len(sequence_sorted))
print(f"Индекс элемента из отсортированного списка: {element_index}")


# ---------------------------------------------------------------------------------------------------------------

# Программа будет сортировать список методом подсчета

# def counting_sort(alist, largest):
#     c = [0] * (largest + 1)
#     for i in range(len(alist)):
#         c[alist[i]] = c[alist[i]] + 1

    # Найдите последний индекс для каждого элемента
    # c[0] = c[0] - 1  # для уменьшения каждого элемента для индексации с отсчетом от нуля
    # for i in range(1, largest + 1):
    #     c[i] = c[i] + c[i - 1]
    #
    # result = [None] * len(alist)

    # Хотя здесь это не требуется, становится необходимым перевернуть список,
    # когда эта функция должна быть стабильной сортировкой.
#     for x in reversed(alist):
#         result[c[x]] = x
#         c[x] = c[x] - 1
#
#     return result
#
#
# alist = input('Введите список (неотрицательный) числа: ').split()
# alist = [int(x) for x in alist]
# k = max(alist)
# sorted_list = counting_sort(alist, k)
# print('Отсортированный список: ', end='')
# print(sorted_list)
