

# import sys

n = int(input())
data = []
max_data = []


for __ in range(n):
    from_input = input()

    if from_input[:4] == 'push':
        number = int(from_input.split()[1])

        data.append(number)
        max_data.append(number if not max_data or number > max_data[-1] else max_data[-1])

    elif from_input == 'pop':
        data.pop()
        max_data.pop()
    elif from_input == 'max':
        if max_data:
            print(max_data[-1])


        


