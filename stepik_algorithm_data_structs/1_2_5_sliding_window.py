

# import sys

# n = int(input())
# numbers = map(int, input().split())
# window = int(input())

# n = 8
# numbers = list(map(int, '2 7 3 1 5 2 6 2'.split()))
# window = 4


n = 3
numbers = list(map(int, '2 1 5'.split()))
window = 1

in_stack = []
out_stack = []


for number in numbers:
    if len(in_stack) < window and not out_stack:
        in_stack_max = number if not in_stack or number >= in_stack[-1][1] else in_stack[-1][1]
        in_stack.append((number, in_stack_max))

        if len(in_stack) == window and not out_stack:

            for __ in range(window):
                poped = in_stack.pop()
                out_stack_max = poped[0] if not out_stack or poped[0] >= out_stack[-1][1] else out_stack[-1][1]
                out_stack.append((poped[0], out_stack_max))

            print(out_stack.pop()[1])

    elif out_stack:
        in_stack_max = number if not in_stack or number >= in_stack[-1][1] else in_stack[-1][1]
        in_stack.append((number, in_stack_max))

        print(max(out_stack.pop()[1], in_stack[-1][1]))




# print(current_max)
#
# for number in numbers[window:]:
#     if current_stack.pop(0)
#     current_max = current_max if current_max > number else number
#     print(current_max)




        


