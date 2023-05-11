# https://www.acmicpc.net/problem/11047

def solve():
    import sys
    N, K = map(int, sys.stdin.readline().split())
    coin = []
    for _ in range(N):
        t = int(sys.stdin.readline())
        coin.append(t)
    
    result_cnt = 0

    while K != 0:
        idx = 0
        for i in range(len(coin)):
            if coin[i] > K:
                break
            idx = i
        
        cnt = K // coin[idx]
        K -= (cnt * coin[idx])
        result_cnt += cnt
    
    print(result_cnt)

if __name__ == "__main__":
    solve()