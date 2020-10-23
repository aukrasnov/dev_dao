

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


n, e, d = map(int, input().split())

forest = [Tree(x) for x in range(n)]

for tree in forest:
    make_set(tree)

# print(forest)

for __ in range(e):
    i, j = map(int, input().split())
    i -= 1
    j -= 1

    union(forest[i], forest[j])


for __ in range(d):
    i, j = map(int, input().split())
    i -= 1
    j -= 1

    if forest[i].parent == forest[j].parent:
        print(0)
        exit()

print(1)



