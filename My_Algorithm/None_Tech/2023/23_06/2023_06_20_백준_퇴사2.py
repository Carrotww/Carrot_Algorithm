# https://www.acmicpc.net/problem/15486

# 브루트 포스 - time out
def solve1():
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    consult_list = []
    for _ in range(N):
        t = list(map(int, input().split()))
        consult_list.append(t)
    
    result = 0

    def check(day):
        nonlocal consult_list

        total_cost = 0
        
        while day < N:
            cost_day, pay = consult_list[day]
            day += cost_day
            if day <= N:
                total_cost += pay
        
        return total_cost
    
    for day in range(N):
        result = max(result, check(day))
    
    print(result)

# dp 풀이 - solve
def solve():
    import sys
    input = sys.stdin.readline
    N = int(input())
    consult_list = []
    for _ in range(N):
        consult_list.append(list(map(int, input().split())))
    
    dp = [0] * (N + 1)
    
    for day in range(N-1, -1, -1):
        time, pay = consult_list[day]
        if time + day <= N:
            dp[day] = max(dp[day+1], pay+dp[day+time])
        else:
            dp[day] = dp[day+1]
    
    print(dp[0])


if __name__ == "__main__":
    solve()