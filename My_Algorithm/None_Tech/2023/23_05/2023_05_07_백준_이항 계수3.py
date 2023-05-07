# https://www.acmicpc.net/problem/11401

def power(a, b, mod):
    result = 1
    while b > 0:
        if b % 2:
            result = (result * a) % mod
        a = (a * a) % mod
        b //= 2
    return result

def solve():
    import sys
    N, K = map(int, sys.stdin.readline().split())
    mod = 1000000007

    factorial = [1] * (N + 1)
    for i in range(2, N + 1):
        factorial[i] = (factorial[i - 1] * i) % mod

    result = (factorial[N] * power(factorial[K], mod - 2, mod) * power(factorial[N - K], mod - 2, mod)) % mod
    print(result)

if __name__ == "__main__":
    solve()