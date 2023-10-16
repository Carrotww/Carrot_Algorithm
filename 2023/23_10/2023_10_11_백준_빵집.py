# https://www.acmicpc.net/problem/3109

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    R, C = map(int, input().split())

    graph = []
    for _ in range(R):
        graph.append(list(input().rstrip()))