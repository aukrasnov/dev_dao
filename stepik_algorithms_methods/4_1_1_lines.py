# По данным  n n отрезкам необходимо найти множество точек минимального размера,
# для которого каждый из отрезков содержит хотя бы одну из точек.
# В первой строке дано число  1 ≤ n ≤ 100 1≤n≤100 отрезков.
# Каждая из последующих  n n строк содержит по два числа  0 ≤ l ≤ r ≤ 1 0 9 0≤l≤r≤10  9  ,
# задающих начало и конец отрезка. Выведите оптимальное число  m m точек и сами  m m точек.
# Если таких множеств точек несколько, выведите любое из них.

# tests
# line = [(3, 6), (1, 3), (2, 5)]
# line = [(4, 7), (1, 3), (2, 5), (5, 6)]
# line = [(5, 6), (4, 7), (3, 8), (2, 9), (1, 10)]
# line = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# line = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# line = [(1, 2), (3, 4), (0, 5)]


def get_common_dots(lines: list):
    lines = sorted(lines, key=lambda x: x[1])
    dots = []
    for i in lines:
        if not dots or i[0] > dots[-1]:
            dots.append(i[1])
    return dots


def read_from_input():
    data = list()
    n = int(input())

    for i in range(n):
        a, b = map(int, input().split())
        data.append((a, b))
    return data


def main():
    data = read_from_input()
    return get_common_dots(data)


if __name__ == "__main__":
    dots = main()
    print(len(dots), ' '.join(map(str, dots)), sep='\n')
