import heapq

# proc_num, tasks = map(int, input().split(' '))
# to_do = [int(x) for x in input().split()]

# proc_num, tasks = (2, 5)
# to_do = [1, 2, 3, 4, 5]


# proc_num, tasks = (4, 20)
# to_do = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# proc_num, tasks = (2, 15)
# to_do = [0, 0, 1, 0, 0, 0, 2, 1, 2, 3, 0, 0, 0, 2, 1]
#
# in_progress = []
# i = proc = 0
#
# while len(in_progress) < proc_num:
#
#     if to_do[i] == 0:
#         print(proc, 0)
#     else:
#         heapq.heappush(in_progress, (0, proc, to_do[i]))
#         proc += 1
#     i += 1
#
# for task in to_do:
#
#     time_start, proc, time_end = heapq.heappop(in_progress)
#     print(proc, time_start)
#     heapq.heappush(in_progress, (time_end, proc, time_end+task))


# while in_progress:
#     time_start, proc, time_end = heapq.heappop(in_progress)
#     print(proc, time_start)


from heapq import heapreplace


proc_num, tasks = map(int, input().split(' '))
to_do = map(int, input().split())

processes = [(0, i) for i in range(proc_num)]

for task in to_do:
    print(*reversed(heapreplace(processes, (processes[0][0] + task, processes[0][1]))))


