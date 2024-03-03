# https://www.acmicpc.net/problem/14002

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    ary = list(map(int, input().split()))

    dp = [[0] * n for _ in range(n)]

    dp = [0] * n
    result = 0
    result_list = []
    for i in range(n):
        temp = ary[i]
        temp_list = [temp]
        cnt = 1
        for j in range(i+1, n):
            if temp < ary[j]:
                cnt += 1
                temp = ary[j]
                temp_list.append(temp)
        if cnt > result:
            result = cnt
            result_list = temp_list

    print(result)
    print(' '.join(map(str, result_list)))


