# #
# l = int(input())
# inp = [int(s) for s in input().split(' ')]
# # inp = [7, 6, 5, 4, 3, 2]
#
#
# switches_number = 0
# out = []
#
#
# def good_heap():
#
#     for i in range(l - 1, 0, -1):
#         parent_index = round((i + 0.5) / 2) - 1
#
#         if i > 0 and inp[i] <= inp[parent_index]:
#             return False
#
#     return True
#
#
# while not good_heap():
#     for i in range(l-1, 0, -1):
#         # print(inp[i])
#
#         parent_index = round((i + 0.5) / 2) - 1
#         # print(inp[i], inp[parent_index])
#
#         while i > 0 and inp[i] < inp[parent_index]:
#             switches_number += 1
#
#             stg = inp[parent_index]
#             inp[parent_index] = inp[i]
#             inp[i] = stg
#
#             out.append([str(parent_index), str(i)])
#             i = parent_index
#             parent_index = round((i + 0.5) / 2) - 1
#
#             # print(inp)
#
# print(switches_number)
#
# for i in out:
#     print(' '.join(i))


n = int(input())
inp = [int(x) for x in input().split()]
output = []


def sift_down(i):
    max_index = i
    left = 2 * i + 1
    if left < n and inp[left] < inp[max_index]:
        max_index = left
    right = 2 * i + 2
    if right < n and inp[right] < inp[max_index]:
        max_index = right
    if i != max_index:
        inp[i], inp[max_index] = inp[max_index], inp[i]
        output.append((i, max_index))
        sift_down(max_index)


# Топим элементы с середины до первого -- остальные уже листы
for k in range((n - 1) // 2, -1, -1):
    print(k)
    sift_down(k)

print(len(output))

for i in output:
    print(*i)

None