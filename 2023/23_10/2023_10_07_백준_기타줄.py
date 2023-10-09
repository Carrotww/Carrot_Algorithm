# https://www.acmicpc.net/problem/1049

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())

    pack = []
    each = []
    for _ in range(m):
        a, b = map(int, input().split())
        pack.append(a)
        each.append(b)

    pack.sort()
    each.sort()

    result = 0
    if n >= 6:
        pack_min = pack[0]
        each_min = each[0] * 6

        value = min(pack_min, each_min)

        pack_cnt = n // 6
        result += (value * pack_cnt)
        n = n % 6

    rest_value = min(pack[0], each[0] * n)
    result += rest_value

    print(result)
