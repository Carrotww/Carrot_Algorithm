# https://www.acmicpc.net/problem/15654

def solve():
    import sys
    n, m = map(int, sys.stdin.readline().split())
    array = list(map(int, sys.stdin.readline().split()))
    array.sort()
    result = []

    def dfs(ary, cnt):
        if cnt == m:
            result.append(ary[:])
            return
        for a in array:
            if a not in ary:
                ary.append(a)
                dfs(ary, cnt+1)
                ary.pop()

    dfs([], 0)
    
    for re in result:
        print(' '.join(map(str, re)))

if __name__ == "__main__":
    solve()