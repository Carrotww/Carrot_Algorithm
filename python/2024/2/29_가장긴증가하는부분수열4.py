# https://www.acmicpc.net/problem/14002

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    ary = list(map(int, input().split()))

    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        dp[i] = 1
        for j in range(i):
            if ary[i] > ary[j]:
                dp[i] = max(dp[i], dp[j]+1)

    result = max(dp)
    max_idx = dp.index(result)
    result_list = [ary[max_idx]]

    print(dp)
    
    temp = result
    for i in range(max_idx, -1, -1):
        if dp[i] == temp - 1:
            temp -= 1
            result_list.append(ary[i])

    print(result)
    print(' '.join(map(str, sorted(result_list))))


