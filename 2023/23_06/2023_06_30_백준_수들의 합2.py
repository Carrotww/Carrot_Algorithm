# https://www.acmicpc.net/problem/2003

def solve():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    count = 0
    interval_sum = 0
    end = 0

    for start in range(n):
        # end 포인터를 이동시키면서 연속된 구간의 합을 구함
        while interval_sum < m and end < n:
            interval_sum += num_list[end]
            end += 1
        
        # 구간의 합이 m과 같으면 경우의 수를 증가시킴
        if interval_sum == m:
            count += 1
        
        # start 포인터를 이동시키면서 구간의 합에서 맨 앞 요소를 제외시킴
        interval_sum -= num_list[start]

    print(count)

if __name__ == "__main__":
    solve()
