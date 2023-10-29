# https://www.acmicpc.net/problem/10942

def solve():
    import sys
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    def check(b):
        if len(b) == 1:
            return True
        if len(b) % 2 == 0:
            start, end = len(b) // 2 - 1, len(b) // 2
            while start >= 0:
                if b[start] != b[end]:
                    return False
                start -= 1
                end += 1
            return True
        else:
            mid = len(b) // 2
            start, end = mid - 1, mid + 1
            while start >= 0:
                if b[start] != b[end]:
                    return False
                start -= 1
                end += 1
            return True

    result = []
    for _ in range(M):
        start, end = map(lambda x: int(x)-1, sys.stdin.readline().split())
        temp = a[start:end+1]
        if check(temp):
            result.append(1)
        else:
            result.append(0)

    for re in result:
        print(re)

def solve():
    import sys
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    
    dp = [[False] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        dp[i][i] = True
    
    for i in range(2, N+1):
        for j in range(N):
            # 이 부분부터 다시 쓰기
            pass

if __name__ == "__main__":
    solve()