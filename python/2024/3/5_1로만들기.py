# https://www.acmicpc.net/problem/1463
# https://bio-info.tistory.com/159

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    dp = [0] * (10**6+2)
    dp[2] = 1
    dp[3] = 1
    for i in range(5, 10**6+1):

        
