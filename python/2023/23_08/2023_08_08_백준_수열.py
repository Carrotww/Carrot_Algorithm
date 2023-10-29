# https://www.acmicpc.net/problem/2559

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    total, k = map(int, input().split())
    temper = list(map(int, input().split()))

    start, end = 0, k-1
    total = sum(temper[:k])
    result = total
    for i in range(len(temper) - k):
        total += temper[i+k] - temper[i]
        result = max(total, result)
    print(result)