# https://www.acmicpc.net/problem/11659

def solve():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    dp = [0] * (n+1)
    dp[0] = num_list[0]

    for i in range(1, n):
        dp[i] = dp[i-1] + num_list[i]

    result = []
    for _ in range(m):
        start, end = map(lambda x: int(x)-1, input().split())
        if start == 0:
            result.append(dp[end])
        else:
            result.append(dp[end]-dp[start-1])
    
    for re in result:
        print(re)

if __name__ == "__main__":
    solve()
