# https://www.acmicpc.net/problem/2230

# 초기 풀이
def solve1():
    import sys
    
    N, M = map(int, sys.stdin.readline().split())
    num_list = []
    for _ in range(N):
        num_list.append(int(sys.stdin.readline()))
    
    num_list.sort()
    
    start, end = 0, 1
    result = float('inf')
    while end != len(num_list):
        temp = num_list[end] - num_list[start]
        if temp >= M:
            result = min(result, temp)
            if start < end:
                start += 1
            else:
                end += 1
        else:
            end += 1
    
    print(result)

# 리펙토링한 풀이
def solve():
    import sys
    
    N, M = map(int, sys.stdin.readline().split())
    num_list = []
    for _ in range(N):
        num_list.append(int(sys.stdin.readline()))
    
    num_list.sort()
    
    start, end = 0, 1
    result = float('inf')
    while end < len(num_list):
        temp = num_list[end] - num_list[start]
        if temp >= M:
            result = min(result, temp)
            start += 1
        else:
            end += 1
        if start == end:
            end += 1

    print(result)

if __name__ == "__main__":
    solve()