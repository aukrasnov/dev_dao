# -*- coding: utf-8 -*-

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
    return fib(n)

# main()

# Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении нужно быть аккуратным с переполнением.
# В данной задаче, впрочем, этой проблемы можно избежать,
# поскольку нас интересует только последняя цифра числа Фибоначчи:
# если 0≤𝑎,𝑏≤9 0 ≤ a , b ≤ 9  — последние цифры чисел 𝐹𝑖 F i  и 𝐹𝑖+1 F i + 1  соответственно,
# то (𝑎+𝑏)mod10 ( a + b ) mod 10  — последняя цифра числа 𝐹𝑖+2 F i + 2 .


def fib_digit(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append((int(str(f[i - 1])[-1:]) + int(str(f[i - 2])[-1:])) % 10)
    return f[n]


def main2():
    n = int(input())
    return fib_digit(n)


# main2()


# Даны целые числа 1≤𝑛≤1018 1 ≤ n ≤ 10 18  и 2≤𝑚≤105 2 ≤ m ≤ 10 5 ,
# необходимо найти остаток от деления 𝑛 n -го числа Фибоначчи на 𝑚 m .

def fib_mod(n, m):
    if n <= 1:
        return n
    fib_num = [0, 1]
    f_0 = 1
    f_1 = 0

    for i in range(n-1):
        temp_f = f_1
        f_1 = f_0 % m
        f_0 = (temp_f + f_1) % m
        fib_num.append(f_0)
        if f_0 == 1 and f_1 == 0:
            index = (n % (i + 1))
            return fib_num[index]

    return f_0


def main3():
    n, m = map(int, input().split())
    return fib_mod(n, m)


# main3()
