# https://www.acmicpc.net/problem/16139

def solve():
    import sys
    input = sys.stdin.readline

    qs = input()
    t = int(input())
    for _ in range(t):
        qa, start, end = input().split()
        start, end = int(start), int(end)

        cnt = 0
        for i in range(start, end+1):
            if qs[i] == qa:
                cnt += 1
        print(cnt)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    qs = input().rstrip()
    t = int(input())

    dp = [[0] * 26 for _ in range(len(qs))]
    dp[0][ord(qs[0])-ord('a')] = 1

    for i in range(1, len(qs)):
        cur_alpa = qs[i]
        for j in range(26):
            dp[i][j] = dp[i-1][j]
        dp[i][ord(cur_alpa)-ord('a')] += 1

    result = []
    for _ in range(t):
        cur_alpa, start, end = input().split()
        start, end = int(start), int(end)
        if start == 0:
            result.append(dp[end][ord(cur_alpa)-ord('a')])
        else:
            result.append(dp[end][ord(cur_alpa)-ord('a')]-dp[start-1][ord(cur_alpa)-ord('a')])

    for r in result:
        print(r)


