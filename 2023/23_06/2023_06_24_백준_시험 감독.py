# https://www.acmicpc.net/problem/13458

def solve():
    import sys
    input = sys.stdin.readline
    n = int(input())
    people = list(map(int, input().split()))
    b, c = map(int, input().split())
    result = 0

    for p in people:
        p -= b
        result += 1

        if p > 0:
            result += p // c
            if p % c != 0:
                result += 1
    print(result)


if __name__ == "__main__":
    solve()
