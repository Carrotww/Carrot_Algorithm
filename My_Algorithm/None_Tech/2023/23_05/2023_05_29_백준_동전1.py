def solve():
    import sys
    sys.setrecursionlimit(20000)
    N, K = map(int, sys.stdin.readline().split())
    coin_list = []
    for _ in range(N):
        coin_list.append(int(sys.stdin.readline()))

    result = [0]
    def dfs(target, total, idx):
        if target == total:
            result[0] += 1
        if target < total:
            return
        for i in range(idx, len(coin_list)):
            dfs(K, total+coin_list[i], i)

    dfs(K, 0, 0)
    print(result[0])

if __name__ == "__main__":
	solve()
