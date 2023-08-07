# # https://www.acmicpc.net/problem/1074

# while 문
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n, r, c = map(int, input().split())
    total_size = 2 ** n
    result = 0

    while n > 0:
        total_size //= 2
        if r >= total_size:
            r -= total_size
            result += (total_size ** 2) * 2
        if c >= total_size:
            c -= total_size
            result += (total_size ** 2) * 1

        n -= 1
    
    print(result)

# 재귀 풀이
def recursion(n, r, c, total_size):
    if n == 0:
        return 0
    mid_size = total_size // 2
    
    temp = 0
    if r >= mid_size:
        temp += (mid_size ** 2) * 2
        r -= mid_size
    if c >= mid_size:
        temp += (mid_size ** 2)
        c -= mid_size
    
    return temp + recursion(n-1, r, c, mid_size)
    
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n, r, c = map(int, input().split())
    total_size = 2 ** n
    result = recursion(n, r, c, total_size)
    print(result)