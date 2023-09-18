# https://www.acmicpc.net/problem/7568

if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    N = int(input())
    info = []
    result = []
    for _ in range(N):
        info.append(list(map(int, input().split())))

    result = []
    for i in range(N):
        cnt = 1
        for j in range(N):
            if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
                cnt += 1
        result.append(str(cnt))

    print(' '.join(result))
