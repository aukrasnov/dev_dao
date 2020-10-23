# Первая строка содержит число  1 ≤ n ≤ 1 0 5 1≤n≤10  5  , вторая — массив  A [ 1 … n ] A[1…n],
# содержащий натуральные числа, не превосходящие  1 0 9 10  9  .
# Необходимо посчитать число пар индексов  1 ≤ i < j ≤ n 1≤i<j≤n, для которых  A [ i ] > A [ j ] A[i]>A[j].
# (Такая пара элементов называется инверсией массива. Количество инверсий в массиве является в некотором смысле
# его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве,
# упорядоченном по убыванию, инверсию образуют каждые два элемента.)


def merge(left_list, right_list, count_invs):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
                count_invs += len(left_list) - left_list_index

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    # print(count_invs)

    return sorted_list, count_invs


def merge_sort(nums, count_invs):

    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums, count_invs

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list, count_invs = merge_sort(nums[:mid], count_invs)
    right_list, count_invs = merge_sort(nums[mid:], count_invs)
    # print(count_invs)

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list, count_invs)


def count_inv_in_row(row):
    count_inv = 0
    row_index = 0

    for i in row:
        for x in row[row_index+1:]:
            if i > x:
                count_inv += 1
        row_index += 1

    return count_inv


def read_input():
    rows_number = int(input())
    row = [int(i) for i in input().split()]
    # row = [2, 3, 9, 2, 9]
    # row = [7, 6, 5, 4, 3, 2, 1]
    # row = [1, 2, 3, 5, 4]

    return row


def main():
    row = read_input()
    random_list_of_nums = merge_sort(row, 0)
    return random_list_of_nums


if __name__ == "__main__":
    answer = main()
    print(answer[1])
