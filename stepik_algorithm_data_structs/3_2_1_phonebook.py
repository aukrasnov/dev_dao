

n = int(input())
db = [None] * 10000000

for i in range(n):
    l = input().split()

    if len(l) == 3:
        command, phone, name = l
    else:
        command, phone = l

    phone = int(phone)

    if command == 'add':
        db[phone] = name
    elif command == 'find':
        out = db[phone] if db[phone] else 'not found'
        print(out)
    else:
        db[phone] = None
