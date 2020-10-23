
def order(i, prev=-2**32):
    stack = []
    while a and i>-1 or stack:
        if i>-1:
            stack.append(i)
            i = a[i][1]
        else:
            i = stack.pop()
            if prev > a[i][0]: return 'INCORRECT'
            prev = a[i][0]
            i = a[i][2]
    return 'CORRECT'
n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
print(order(0))
