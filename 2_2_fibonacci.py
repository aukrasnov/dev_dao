# Дано целое число 1≤𝑛≤40 1 ≤ n ≤ 40 , необходимо вычислить 𝑛 n -е число Фибоначчи
# (напомним, что 𝐹0=0 F 0 = 0 , 𝐹1=1 F 1 = 1  и 𝐹𝑛=𝐹𝑛−1+𝐹𝑛−2
#         F n = F n − 1 + F n − 2  при 𝑛≥2 n ≥ 2 ).


def fib(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
