# Дано целое число  1 ≤ n ≤ 1 0 3 1≤n≤10  3   и массив  A [ 1 … n ] A[1…n] натуральных чисел,
# не превосходящих  2 ⋅ 1 0 9 2⋅10  9  . Выведите максимальное  1 ≤ k ≤ n 1≤k≤n,
# для которого найдётся подпоследовательность  1 ≤ i 1 < i 2 < … < i k ≤ n 1≤i  1 ​   <i  2 ​   <…<i  k ​   ≤n длины  k k,
# в которой каждый элемент делится на предыдущий (формально: для  всех  1 ≤ j < k 1≤j<k,  A [ i j ] ∣ A [ i j + 1 ]
# A[i  j ​   ]∣A[i  j+1 ​   ]).


def read_input():
    delim = int(input())
    list_ = [int(i) for i in input().split()]

    return delim, list_


def _lis(arr, delim):

    if delim == 0:
        return 0

    b = [1] * delim
    for i in range(delim):
        for j in range(i - 1, -1, -1):
            if arr[i] % arr[j] == 0 and b[j] + 1 > b[i]:
                b[i] = b[j] + 1

    return max(b)


def main(arr, delim):
    return _lis(arr, delim)


if __name__ == "__main__":
    delim, list_ = read_input()
    print(main(list_, delim))
    # arr = [3, 6, 7, 12]
    # delim = 4
    # n = len(arr)
    # print(main(arr))
