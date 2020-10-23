# По данным  n n отрезкам необходимо найти множество точек минимального размера,
# для которого каждый из отрезков содержит хотя бы одну из точек.
# В первой строке дано число  1 ≤ n ≤ 100 1≤n≤100 отрезков.
# Каждая из последующих  n n строк содержит по два числа  0 ≤ l ≤ r ≤ 1 0 9 0≤l≤r≤10  9  ,
# задающих начало и конец отрезка. Выведите оптимальное число  m m точек и сами  m m точек.
# Если таких множеств точек несколько, выведите любое из них.

# tests
case1 = (50, [(60, 20), (100, 50), (120, 30)])


def read_from_input():
    items_number, bag_volume = map(int, input().split())
    data = []

    for item in range(items_number):
        item_price, item_volume = map(int, input().split())
        data.append((item_price, item_volume))
    return bag_volume, data


def bag_items_max_price(space_left, items: list):
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    taken_items_price = 0
    for i in items:
        if space_left > 0:
            taken_items_price += i[0]/i[1]*min(i[1], space_left)
            space_left -= i[1]
        else:
            return round(taken_items_price, 3)
    return round(taken_items_price, 3)


def main():
    bag_volume, items = read_from_input()
    # bag_volume, items = case1
    return bag_items_max_price(bag_volume, items)


if __name__ == "__main__":
    print(main())
