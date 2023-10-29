# https://www.acmicpc.net/problem/9095

def solve():
    import sys
    N = int(sys.stdin.readline())
    result = [0] * N
    
    def dfs(target, num, i):
        if num == target:
            result[i] += 1
            return
        if num > target:
            return
        for plus in (1, 2, 3):
            temp = num + plus
            dfs(target, temp, i)
            temp -= plus
    
    for i in range(N):
        target = int(sys.stdin.readline())
        dfs(target, 0, i)
    
    for re in result:
        print(re)

if __name__ == "__main__":
    solve()