# https://www.acmicpc.net/problem/13144

# 1번째 풀이 brute force -> time out
# n 이 십만이라 당연히 시간초과 그냥 해봄
def solve():
    import sys

    input = sys.stdin.readline

    n = int(input())
    array = list(map(int, input().split()))
    cnt = n

    for i in range(n-1):
        start, end = i, i+1
        check_set = {array[start]}
        while end < n:
            if array[end] not in check_set:
                check_set.add(array[end])
                cnt += 1
            end += 1
    print(cnt)


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    n = int(input())
    array = list(map(int, input().split()))

    start, end = 0, 0
    check = [False] * 100001
    cnt = 0
    
    while start < n and end < n:
        if check[array[end]] == False:
            check[array[end]] = True
            end += 1
            cnt += (end - start)
        else:
            check[array[start]] = False
            start += 1
    
    print(cnt)