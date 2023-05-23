# https://www.acmicpc.net/problem/2217

def solve():
    import sys
    N = int(sys.stdin.readline())
    a = []
    for _ in range(N):
        a.append(int(sys.stdin.readline()))
    
    result = 0
    a.sort()
    for i in range(len(a)):
        temp = a[i] * (N - i)
        result = max(result, temp)
    
    print(result)

if __name__ == "__main__":
    solve()