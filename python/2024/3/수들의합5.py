# https://www.acmicpc.net/problem/2018

def two1(target):
    result, total, end = 0, 0, 1

    for start in range(1, target+1):
        while total < target:
            total += end
            end += 1
        if total == target:
            result += 1
        total -= start

    return result

def two2(target):
    result, total, end = 0, 0, 1

    for start in range(1, target+1):
        while total <= target:
            if total == target:
                result += 1
                break
            total += end
            end += 1
        total -= start
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    target = int(input())

    print(two1(target))

