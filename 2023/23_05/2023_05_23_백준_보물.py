# https://www.acmicpc.net/problem/1026

def solve():
    import sys
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    result = 0
    A.sort()
    B.sort(reverse=True)
    for a, b in zip(A, B):
        result += a * b
    
    print(result)

if __name__ == "__main__":
    solve()