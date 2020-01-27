# Первая строка входа содержит число операций  1 ≤ n ≤ 1 0 5 1≤n≤10  5  .
# Каждая из последующих  n n строк задают операцию одного из следующих двух типов:
# I n s e r t Insert  x x, где  0 ≤ x ≤ 1 0 9 0≤x≤10  9   — целое число;
# E x t r a c t M a x ExtractMax.
# Первая операция добавляет число  x x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.


# def read_input():
#     rows_number = int(input())
#
#     operations_to_do = []
#     for i in range(rows_number):
#         operations_to_do.append(str(input()))
#
#     return operations_to_do
#
#
# def insert(row, number):
#     row.append(int(number))
#     row = sorted(row, reverse=True)
#
#     return row
#
#
# def extract_max(row):
#     extracted_value = row.pop(0)
#     return row, extracted_value
#
#
# def execute(operations_to_do):
#     answer = []
#     row = []
#     for i in operations_to_do:
#         if i == 'ExtractMax':
#             row, extracted_value = extract_max(row)
#             answer.append(extracted_value)
#         else:
#             row = insert(row, i.split(' ')[1])
#
#     return answer
#
#
# def main():
#     operations_to_do = read_input()
#     # operations_to_do = ['Insert 200', 'Insert 10', 'ExtractMax', 'Insert 5', 'Insert 500', 'ExtractMax']
#     # operations_to_do = ['Insert 200', 'Insert 10', 'Insert 5', 'Insert 500', 'ExtractMax', 'ExtractMax', 'ExtractMax', 'ExtractMax']
#
#     return execute(operations_to_do)
#
#
# if __name__ == "__main__":
#     # main()
#     answer = main()
#     for i in answer:
#         print(i)
#


import heapq


def read_input():
    rows_number = int(input())

    operations_to_do = []
    for i in range(rows_number):
        operations_to_do.append(str(input()))

    return operations_to_do


def insert(row, number):
    row.append(int(number))
    row = sorted(row, reverse=True)

    return row


def extract_max(row):
    extracted_value = row.pop(0)
    return row, extracted_value


def execute(operations_to_do):
    answer = []
    heap = []
    heapq.heapify(heap)
    for i in operations_to_do:
        if i == 'ExtractMax':
            answer.append(int(heapq.heappop(heap)) * -1)
        else:
            heapq.heappush(heap, int(i.split(' ')[1]) * -1)

    return answer


def main():
    operations_to_do = read_input()
    # operations_to_do = ['Insert 200', 'Insert 10', 'ExtractMax', 'Insert 5', 'Insert 500', 'ExtractMax']
    # operations_to_do = ['Insert 200', 'Insert 10', 'Insert 5', 'Insert 500', 'ExtractMax', 'ExtractMax', 'ExtractMax', 'ExtractMax']

    return execute(operations_to_do)


if __name__ == "__main__":
    # main()
    answer = main()
    for i in answer:
        print(i)

