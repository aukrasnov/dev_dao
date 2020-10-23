
def in_order(n):
    if tree[n][1] >= 0:
        in_order(tree[n][1])
    print(tree[n][0], end=' ')
    if tree[n][2] >= 0:
        in_order(tree[n][2])


def pre_order(n):
    print(tree[n][0], end=' ')
    if tree[n][1] >= 0:
        pre_order(tree[n][1])
    if tree[n][2] >= 0:
        pre_order(tree[n][2])


def post_order(n):
    if tree[n][1] >= 0:
        post_order(tree[n][1])
    if tree[n][2] >= 0:
        post_order(tree[n][2])
    print(tree[n][0], end=' ')


tree = []
n = int(input())

for i in range(n):
    tree.append([int(s) for s in input().split()])

in_order(0)
print()
pre_order(0)
print()
post_order(0)
print()
