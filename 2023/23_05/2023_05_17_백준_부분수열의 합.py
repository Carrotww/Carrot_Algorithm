# https://www.acmicpc.net/problem/1182

# 틀렸던 점
# 1. total이 K보다 커져도 음수가 있을 수 있으므로 total > K return 조건은 없어야함
# 2. total == K 후 return을 하게되면 추가로 있는 같인 음수 양수 조건을 서치 불가능함

def solve():
    import sys
    sys.setrecursionlimit(1000)
    
    N, K = map(int, sys.stdin.readline().split())
    num_list = list(map(int, sys.stdin.readline().split()))
    result = 0

    def dfs(idx, total, cnt):
        nonlocal result
        if total == K and cnt > 0:
            result += 1
        
        for i in range(idx, N):
            total += num_list[i]
            dfs(i+1, total, cnt+1)
            total -= num_list[i]
    
    dfs(0, 0, 0)
    print(result)
    
if __name__ == "__main__":
    solve()