# https://www.acmicpc.net/problem/1158

def solve():
    import sys
    N, K = map(int, sys.stdin.readline().split())
    num_list = [x for x in range(1, N+1)]
    result = []
    idx = 0
    
    for i in range(N):
        idx += (K-1)
        if idx >= N:
            idx %= N
        result.append(str(num_list.pop(idx)))
        N -= 1

    print("<",", ".join(result)[:],">", sep='')

if __name__ == "__main__":
    solve()