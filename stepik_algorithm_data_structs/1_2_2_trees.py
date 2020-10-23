

def find_parent(i):

    if h[i] != 0:
        return h[i]
    elif l[i] == -1:
        h[i] = 1
    else:
        h[i] = 1 + find_parent(l[i])

    return h[i]


n = int(input())
l = [int(x) for x in input().split()]
h = [0]*n


for i in range(n):
    find_parent(i)

print(max(h))

# elements = [-1, 0, 4, 0, 3]
# elements = [4, -1, 4, 1, 1]
# elements = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]
# elements = [2, 2, 3, 5, 5, 7, 7, 9, 9, -1]
# elements = [2, 2, 3, 5, 5, 7, 7, 9, 9, -1]
# elements = [-1]
# elements = [-1, 0, 1, 1]
# elements = [4, -1, 4, 1, 1]
# elements = [[e, 0] for e in elements]

# print([(e, 0) for e in elements])
# print(main())



# def fill(i):
#     if h[i]!=0:
#         return h[i]
#     if l[i]==-1:
#         h[i] = 1
#     else:
#         h[i] = 1+fill(l[i])
#     return h[i]
#
#
# n = int(input())
# l = [int(x) for x in input().split()]
# h = [0]*n
# for i in range(n):
#     fill(i)
# print(max(h))