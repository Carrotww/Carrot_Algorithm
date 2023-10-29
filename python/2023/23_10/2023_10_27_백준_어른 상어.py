# https://www.acmicpc.net/problem/19237

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    # n -> n * n 격자
    # m -> 상어 수
    # k -> 냄새가 사라지기까지의 시간
    n, m, k = map(int, input().split())
    graph = []
    shark = [-1] * (m + 1)
    priority = [[] for _ in range(m + 1)]
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    