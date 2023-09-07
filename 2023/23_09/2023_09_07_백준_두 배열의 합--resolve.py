# https://www.acmicpc.net/problem/2143

def binary_right_index(give_list, target):
    start, end = 0, len(give_list)
    while start < end:
        mid = (start + end) // 2
        val = give_list[mid]
        if val <= target:
            start = mid + 1
        else:
            end = mid
    return start

def binary_left_index(give_list, target):
    start, end = 0, len(give_list)
    while start < end:
        mid = (start + end) // 2
        val = give_list[mid]
        if val < target:
            start = mid + 1
        else:
            end = mid
    return start

def solve(give_list, target):
    return binary_right_index(give_list, target) - binary_left_index(give_list, target)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    T = int(input())
    N = int(input())
    n_list = list(map(int, input().split()))
    M = int(input())
    m_list = list(map(int, input().split()))

    a = []
    b = []

    for i in range(N):
        start = n_list[i]
        a.append(start)
        for j in range(i+1, N):
            start += n_list[j]
            a.append(start)
    
    for i in range(M):
        start = m_list[i]
        b.append(start)
        for j in range(i+1, M):
            start += m_list[j]
            b.append(start)
    
    result = 0
    b.sort()
    for val in a:
        result += solve(b, T-val)
    print(result)