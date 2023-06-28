# https://www.acmicpc.net/problem/1261

def solve():
    import sys
    input = sys.stdin.readline

    col, row = map(int, input().split())
    graph = []
    for r in range(row):
        temp = input().split().pop()
        temp = [int(x) for x in temp]
        graph.append(temp)


if __name__ == "__main__":
    solve()
