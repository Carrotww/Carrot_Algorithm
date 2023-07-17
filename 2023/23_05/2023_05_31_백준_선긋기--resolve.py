# https://www.acmicpc.net/problem/2170

def solve():
    import sys
    N = int(sys.stdin.readline())

    dot_list = []
    for _ in range(N):
        dot_list.append(list(map(int, sys.stdin.readline().split())))
    dot_list.sort()
    start, end = dot_list[0][0], dot_list[0][1]
    result = 0

    for i in range(1, N):
        if dot_list[i][0] <= end:
            end = max(end, dot_list[i][1])
        else:
            result += end - start
            start, end = dot_list[i][0], dot_list[i][1]
    
    result += end - start
    print(result)

if __name__ == "__main__":
    solve()