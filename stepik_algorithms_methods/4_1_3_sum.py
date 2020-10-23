# По данному числу  1 ≤ n ≤ 1 0 9 1≤n≤10  9   найдите максимальное число  k k,
# для которого  n n можно представить как сумму  k k различных натуральных слагаемых.
# Выведите в первой строке число  k k, во второй —  k k слагаемых.


def read_input():
    number = int(input())
    return number


def diff_numbers(remaining):
    answer = []
    number = 1

    while True:
        if remaining == 0:
            break

        if remaining - number <= number:
            answer.append(remaining)
            break

        answer.append(number)
        remaining -= number
        number += 1

    return answer


def main():
    data = read_input()
    # data = 8

    return diff_numbers(data)


if __name__ == "__main__":
    answer = main()
    print(len(answer))
    print(' '.join(map(str, answer)))
