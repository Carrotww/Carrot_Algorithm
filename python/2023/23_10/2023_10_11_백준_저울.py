# https://www.acmicpc.net/problem/2437

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    ary = list(map(int, input().split()))

    ary.sort()

    target = 1

    for a in ary:
        if target < a:
            break
        else:
            target += a
    print(target)