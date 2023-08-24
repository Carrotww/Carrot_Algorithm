# https://www.acmicpc.net/problem/16401

def divide(n):
    # n으로 N명의 사람에게 snack을 나눠줄 수 있는지
    if n == 0:
        return True
    cnt = 0
    for s in snack:
        cnt += (s // n)
    return cnt >= M

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    M, N = map(int, input().split())
    snack = list(map(int, input().split()))
    result = 0

    left, right = 0, max(snack)
    while left <= right:
        mid = (left + right) // 2
        if divide(mid):
            left = mid + 1
            result = mid
        else:
            right = mid - 1
    print(result)