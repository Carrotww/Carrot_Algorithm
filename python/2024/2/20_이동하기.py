# https://www.acmicpc.net/problem/11048

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    r, c = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(r)]

    move = [(1, 0), (0, 1), (1, 1)]
