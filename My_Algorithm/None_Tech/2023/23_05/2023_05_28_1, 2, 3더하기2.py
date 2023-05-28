# https://www.acmicpc.net/problem/9095

def solve():
    import sys
    N = int(sys.stdin.readline())
    result = [0] * N
    
    def dfs(target, num, idx):
        if num == target:
            result[idx] += 1
        if num > target:
            return
        for i in (1, 2, 3):
            dfs(target, num+i, idx)
    
    for i in range(N):
        num = int(sys.stdin.readline())
        dfs(num, 0, i)
    
    for re in result:
        print(re)

if __name__ == "__main__":
    solve()