# https://www.acmicpc.net/problem/1654

def solve():
    import sys
    
    K, N = map(int, sys.stdin.readline().split())
    cable = []
    for _ in range(K):
        cable.append(int(sys.stdin.readline()))
    
    start = 0
    end = max(cable)

    result = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        
        for c in cable:
            cnt += c // mid
        
        if cnt >= N:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    print(result)

if __name__ == "__main__":
    solve()