# https://www.acmicpc.net/problem/6236

def check(money):
    if money < max(ary):
        return False
    cnt = 1
    cur_money = money
    for need_money in ary:
        if cur_money < need_money:
            cur_money = money
            cnt += 1
        cur_money -= need_money
    return cnt <= m

def binary_search():
    start, end = 1, sum(ary)+1
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

