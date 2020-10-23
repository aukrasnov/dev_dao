

class Tree:
    def __init__(self, size, parent=0):
        self.size = size
        self.parent = parent


def make_set(x):
    x.parent = x


def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        y_root.parent = x_root
        x_root.size = x_root.size + y_root.size

    return x_root.size


def find(x):

    if x.parent == x:
        return x
    else:
        x.parent = find(x.parent)
        return x.parent


# count_tables, count_requests = map(int, '5 5'.split())
# forest = [Tree(int(x)) for x in '1 1 1 1 1'.split()]
# requests = [(3, 5), (2, 4), (1, 4), (5, 4), (5, 3)]

# count_tables, count_requests = map(int, '6 4'.split())
# tables_sizes = [int(x) for x in '10 0 5 0 3 3'.split()]
# requests = [(6, 6), (6, 5), (5, 4), (4, 3)]

count_tables, count_requests = map(int, input().split())
tables_sizes = [int(x) for x in input().split()]
requests = []
for i in range(count_requests):
    requests.append(map(int, input().split()))

forest = [Tree(x) for x in tables_sizes]
max_size = max(tables_sizes)

for tree in forest:
    make_set(tree)

for r in requests:
    destination, source = r
    destination, source = destination - 1, source - 1
    max_size = max(union(forest[destination], forest[source]), max_size)
    print(max_size)









