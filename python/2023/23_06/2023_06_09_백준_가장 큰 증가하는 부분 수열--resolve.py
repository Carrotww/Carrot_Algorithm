# https://www.acmicpc.net/problem/11055

def solve():
    import sys
    N = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))

    dp = [0] * N
    dp[0] = array[0]
    
    for i in range(1, N):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i], dp[j])
        dp[i] += array[i]
    
    print(max(dp))

if __name__ == "__main__":
    solve()