# Первая строка входа содержит целые числа  1 ≤ W ≤ 1 0 4 1≤W≤10  4   и  1 ≤ n ≤ 300 1≤n≤300 —
# вместимость рюкзака и число золотых слитков. Следующая строка содержит  n n целых чисел  0 ≤ w 1 , … ,
# w n ≤ 1 0 5 0≤w  1 ​   ,…,w  n ​   ≤10  5  , задающих веса слитков. Найдите максимальный вес золота,
# который можно унести в рюкзаке.


def sack_bu(weight, count_items, items_value):
    d = [[0] * (weight+1) for _ in range(count_items)]
    for i in range(count_items):
        for w in range(weight+1):
            d[i][w] = d[i - 1][w]
            if items_value[i] <= w:
                # print(d[i - 1][weight - items_value[i]])
                d[i][w] = max(d[i][w], d[i - 1][w - items_value[i]] + items_value[i])

    return d[-1][-1]


def main():
    weight, count_items = (int(i) for i in input().split())
    items_value = [int(i) for i in input().split()]
    # weight, count_items = (10, 3)
    # items_value = [1, 4, 8]

    return sack_bu(weight, count_items, items_value)


if __name__ == "__main__":
    # test()
    print(main())
