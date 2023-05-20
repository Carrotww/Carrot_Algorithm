# https://www.acmicpc.net/problem/1463

# 상향식
def solve():
    import sys
    num = int(sys.stdin.readline())

    dp = [0] * (num + 1)

    for i in range(2, num+1):
        dp[i] = dp[i-1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
    
    print(dp[num])

# 하향식
def solve1():
    import sys
    num = int(sys.stdin.readline())
    
    dp = [float('inf')] * (num + 1)
    dp[num] = 0
    
    for i in range(num, 0, -1):
        if i % 3 == 0:
            dp[i//3] = min(dp[i]+1, dp[i//3])
        if i % 2 == 0:
            dp[i//2] = min(dp[i]+1, dp[i//2])
        dp[i-1] = min(dp[i]+1, dp[i-1])
    
    print(dp[1])

if __name__ == "__main__":
    solve()
