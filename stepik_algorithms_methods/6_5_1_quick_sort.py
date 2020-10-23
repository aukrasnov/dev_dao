# В первой строке задано два целых числа  1 ≤ n ≤ 50000 1≤n≤50000 и  1 ≤ m ≤ 50000 1≤m≤50000 — количество отрезков
# и точек на прямой, соответственно. Следующие  n n строк содержат по два целых числа  a i a  i ​    и  b i b  i ​
# ( a i ≤ b i a  i ​   ≤b  i ​   ) — координаты концов отрезков. Последняя строка содержит  m m целых чисел — координаты
# точек. Все координаты не превышают  1 0 8 10  8   по модулю. Точка считается принадлежащей отрезку, если она находится
# внутри него или на границе. Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
from bisect import bisect_left, bisect_right
import random

def read_input():
    count_lines, count_points = input().split()
    line_starts = list()
    line_ends = list()

    for i in range(int(count_lines)):
        input_ = input().split()
        line_starts.append(int(input_[0]))
        line_ends.append(int(input_[1]))
    points = input().split()
    points = [int(p) for p in points]

    return line_starts, line_ends, points


# def partition(xs, start, end):
#     follower = leader = start
#     while leader < end:
#         if xs[leader] <= xs[end]:
#             xs[follower], xs[leader] = xs[leader], xs[follower]
#             follower += 1
#         leader += 1
#     xs[follower], xs[end] = xs[end], xs[follower]
#     return follower
#
#
# def _quicksort(xs, start, end):
#     if start >= end:
#         return
#     p = partition(xs, start, end)
#     _quicksort(xs, start, p - 1)
#     _quicksort(xs, p + 1, end)
#
#
# def quicksort(xs):
#     _quicksort(xs, 0, len(xs) - 1)


def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = random.choice(array)
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)
    else:
        return array


def point_in_line(point, lines):
    answer = 0
    for line in lines:
        if point >= line[0] and point <= line[1]:
            answer += 1

    return answer


def count_less_or_greater(point, line_starts):
    n = 0
    for p in line_starts:
        if p <= point:
            n += 1
        else:
            return n
    return n


def count_less(point, line_ends):
    m = 0
    for p in line_ends:
        if p < point:
            m += 1
        else:
            return m
    return m


def main():
    line_starts, line_ends, points = read_input()
    line_starts = quicksort(line_starts)
    line_ends = quicksort(line_ends)

    answer = []
    for p in points:
        n = bisect_right(line_starts, p)
        m = bisect_left(line_ends, p)
        answer.append(str(n - m))

    return answer


if __name__ == "__main__":
    print(' '.join(main()))
