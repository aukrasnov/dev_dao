# Первая строка содержит число  1 ≤ n ≤ 1 0 4 1≤n≤10  4  , вторая —  n n натуральных чисел, не превышающих 10.
# Выведите упорядоченную по неубыванию последовательность этих чисел.

from bisect import bisect_left, bisect_right
import random


def read_input():
    useless_number = int(input())
    list_ = [int(i) for i in input().split()]

    # list_ = [2, 3, 9, 2, 9]
    return list_


def sort_d(list_):
    d = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

    for i in list_:
        d[i] += 1

    answer_str = ''

    for i in d:
        answer_str += '{} '.format(i) * d[i]

    return answer_str


def main():
    answer = sort_d(read_input())

    return answer


if __name__ == "__main__":
    print(main())
