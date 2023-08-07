# # https://www.acmicpc.net/problem/1074

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