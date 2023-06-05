# https://www.acmicpc.net/problem/15652

def solve():
    import sys
    n, m = map(int, sys.stdin.readline().split())
    a = [x for x in range(1, n+1)]
    
    def dfs(idx, cnt):
        if cnt == m:
            print(' '.join(map(str, a[idx-m:idx+1])))
            return
        for i in range(idx, n):
            dfs(i, cnt+1)
    dfs(0, 0)

if __name__ == "__main__":
    solve()