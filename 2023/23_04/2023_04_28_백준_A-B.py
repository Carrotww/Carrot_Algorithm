# https://www.acmicpc.net/problem/16953

# 두 번째 풀이
def solve():
    import sys
    A, B = map(int, sys.stdin.readline().split())
    
    def dfs(num, cnt, min_cnt):
        if num > B:
            return min_cnt
        if num == B:
            return min(cnt, min_cnt)
        
        min_cnt = dfs(int(str(num)+str(1)), cnt+1, min_cnt)
        min_cnt = dfs(num*2, cnt+1, min_cnt)

        return min_cnt
    
    result = dfs(A, 1, B+1)

    if result == B+1:
        print(-1)
    else:
        print(result)

# 첫 번째 풀이
def solve():
    import sys
    A, B = map(int, sys.stdin.readline().split())
    result = []
    
    def dfs(num, cnt):
        if num > B:
            result.append(-1)
            return
        if num == B:
            result.append(cnt)
            return
        
        dfs(int(str(num)+str(1)), cnt+1)
        dfs(num*2, cnt+1)
    
    dfs(A, 1)

    answer = -1
    for i in result:
        if i != -1:
            answer = i
            break
    
    print(answer)

if __name__ == "__main__":
    solve()