# https://www.acmicpc.net/problem/14719

def solve():
    import sys
    H, W = map(int, sys.stdin.readline().split())
    rain = list(map(int, sys.stdin.readline().split()))
    result = 0

    for i in range(1, len(rain)-1):
        left_max = max(rain[:i])
        right_max = max(rain[i+1:])

        center = min(left_max, right_max)

        if rain[i] < center:
            result += (center - rain[i])
            
    print(result)

if __name__ == "__main__":
    solve()