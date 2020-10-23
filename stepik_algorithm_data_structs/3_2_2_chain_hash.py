# put your python code here


d = [[] for _ in range(int(input()))]

for _ in range(int(input())):
    cmd, v = input().split()

    if cmd == 'check':
        print(*d[int(v)])
    else:
        h = sum([ord(s)*263**i for i, s in enumerate(v)]) % 1000000007 % len(d)
        if cmd == 'add' and not v in d[h]:  d[h].insert(0,v)
        elif cmd == 'find': print('yes' if v in d[h] else 'no')
        elif cmd == 'del' and v in d[h]: d[h].remove(v)
