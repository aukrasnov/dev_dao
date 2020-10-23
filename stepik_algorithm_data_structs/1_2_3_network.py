
import collections

size, n = map(int, input().split())
buffer = collections.deque([0] * size)
max_buffer = 0


for __ in range(n):
    arrival, duration = map(int, input().split())

    if buffer[-1] <= arrival:
        start_time = max(max_buffer, arrival)
        finish_time = start_time + duration
        buffer.appendleft(finish_time)
        print(start_time)
        buffer.pop()

        max_buffer = max_buffer if finish_time < max_buffer else finish_time

    else:
        print(-1)

    # for i in range(len(buffer), 1, -1):
    #
    #     if buffer[i-1] < buffer[i-2]:
    #         print(buffer, i)
    #         buffer.pop()
    #         buffer = [0] + buffer
    #         print('HERE')






    # print(cpu)
    # print(arrival)

# buffer = [0]
#
# for i in range(len(buffer), 1, -1):
#     print(i)
#     if buffer[i - 1] < buffer[i - 2]:
#         buffer.pop()
#         buffer = [0] + buffer


# l = [1, 2, 3]
#
# for i in l[::-1]:
#     print(i)
#     if i == 3:
#         print(l.pop())
#
# print(l)
