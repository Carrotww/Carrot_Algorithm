# https://www.acmicpc.net/problem/2212

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    K = int(input())
    sensor = sorted(list(map(int, input().split())))
    sensor_diff = sorted([sensor[x+1]-sensor[x] for x in range(N - 1)])
    print(sum(sensor_diff[:N-K]))
