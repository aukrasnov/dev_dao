# Дано целое число  1 ≤ n ≤ 1 0 3 1≤n≤10  3   и массив  A [ 1 … n ] A[1…n] натуральных чисел,
# не превосходящих  2 ⋅ 1 0 9 2⋅10  9  . Выведите максимальное  1 ≤ k ≤ n 1≤k≤n,
# для которого найдётся подпоследовательность  1 ≤ i 1 < i 2 < … < i k ≤ n 1≤i  1 ​   <i  2 ​   <…<i  k ​   ≤n длины  k k,
# в которой каждый элемент делится на предыдущий (формально: для  всех  1 ≤ j < k 1≤j<k,  A [ i j ] ∣ A [ i j + 1 ]
# A[i  j ​   ]∣A[i  j+1 ​   ]).


def read_input():
    delim = int(input())
    list_ = [int(i) for i in input().split()]

    return list_

def longest_increasing_subsequence(X):

    N = len(X)
    P = [0] * N
    M = [0] * (N + 1)
    L = 0
    for i in range(N):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo + hi) // 2
            if (X[M[mid]] >= X[i]):
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo
        P[i] = M[newL - 1]
        M[newL] = i

        if (newL > L):
            L = newL

    S = []
    k = M[L]
    answer = []
    for i in range(L - 1, -1, -1):
        S.append(X[k])
        answer.append(str(k+1))
        k = P[k]
    return answer


def main(arr):
    return longest_increasing_subsequence(arr)


if __name__ == "__main__":
    list_ = read_input()
    # list_ = [5, 3, 4, 4, 2]
    b = longest_increasing_subsequence(list_)
    print(len(b))
    print(' '.join(reversed(b)))
