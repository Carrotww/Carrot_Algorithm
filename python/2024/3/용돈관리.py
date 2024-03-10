# https://www.acmicpc.net/problem/6236

def check(money):
    cur_money = money
    cnt = 1
    for need_money in ary:
        if cur_money >= need_money:
            cur_money -= need_money
        else:
            if need_money > money:
                cur_cnt = need_money // money
                if need_money % money:
                    cur_cnt += 1
                cur_money = (cur_cnt * money) - need_money
                cnt += cur_cnt
            else:
                cur_money = money - need_money
                cnt += 1

    return cnt <= m

def binary_search():
    start, end = 1, 10000 * 100000
    result = end
    while start <= end:
        mid = (start + end) // 2
        if check(mid):
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    ary = []
    for _ in range(n):
        ary.append(int(input()))

    print(binary_search())

