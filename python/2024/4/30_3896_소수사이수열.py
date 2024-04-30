# https://www.acmicpc.net/problem/3896

def find_decimal(num):
    if num == 1 or num == 2:
        return True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(num):
    result = 0
    if find_decimal(num):
        result = 0
    else:
        min_decimal,  max_decimal = num - 1, num + 1
        while not find_decimal(min_decimal):
            min_decimal -= 1

        while not find_decimal(max_decimal):
            max_decimal += 1

        result = max_decimal - min_decimal

    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    t = int(input())
    result = []

    for _ in range(t):
        num = int(input())
        result.append(solution(num))

    for r in result:
        print(r)


