# https://www.acmicpc.net/problem/14427

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    ary = list(map(int, input().split()))
    t = int(input())
    result = []
    for _ in range(t):
        temp = list(map(int, input().split()))
        if temp[0] == 1:
            index = temp[1] - 1
            val = temp[2]
            ary[index] = val
        else:
            result.append(ary.index(min(ary)) + 1)

    for r in result:
        print(r)


