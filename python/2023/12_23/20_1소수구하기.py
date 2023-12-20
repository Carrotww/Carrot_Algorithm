# https://www.acmicpc.net/problem/1929

def check(num):
    if num == 1:
        return False
    for i in range(2, int(num ** (0.5)) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    import sys
    m, n = map(int, input().split())

    for num in range(m, n+1):
        if check(num):
            print(num)
