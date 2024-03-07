# https://www.acmicpc.net/problem/15565

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    ary = list(map(int, input().split()))
    lion_index_ary = []
    for i in range(n):
        if ary[i] == 1:
            lion_index_ary.append(i)

    if len(lion_index_ary) < k:
        print(-1)
    else:
        result = float('inf')
        for i in range(0, len(lion_index_ary)-k+1):
            result = min(result, lion_index_ary[i+k-1]-lion_index_ary[i]+1)
        print(result)


