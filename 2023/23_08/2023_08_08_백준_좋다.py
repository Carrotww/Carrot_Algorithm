# https://www.acmicpc.net/problem/1253

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    temp = list(map(int, input().split()))
    temp.sort()

    result = 0
    for i in range(n):
        temp_list = temp[0:i] + temp[i+1:]
        compare_val = temp[i]

        start, end = 0, n-2
        while start < end:
            sum_t = temp_list[start] + temp_list[end]
            if sum_t == compare_val:
                result += 1
                break
            elif sum_t < compare_val:
                start += 1
            else:
                end -= 1

    print(result)
