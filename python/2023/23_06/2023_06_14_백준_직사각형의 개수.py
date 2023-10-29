# https://www.acmicpc.net/problem/2171

def solve():
    import sys
    from itertools import combinations
    from collections import Counter
    N = int(sys.stdin.readline())

    dot_list = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        dot_list.append([x, y])

    row_dict = dict()
    for x, y in dot_list:
        if y not in row_dict:
            row_dict[y] = [x]
        else:
            row_dict[y].append(x)

    for key, val in row_dict.items():
        temp = list(map(lambda x: (x[0], x[1]) if x[0] < x[1] else (
            x[1], x[0]), list(combinations(val, 2))))
        row_dict[key] = temp

    count_square_dict = dict()

    for val in row_dict.values():
        for v in val:
            if v not in count_square_dict:
                count_square_dict[v] = 1
            else:
                count_square_dict[v] += 1

    result = 0
    for val in count_square_dict.values():
        if val >= 2:
            result += (val * (val - 1)) // 2

    print(result)

def solve1():
    import sys
    from itertools import combinations
    from collections import Counter
    N = int(sys.stdin.readline())

    dot_list = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        dot_list.append([x, y])

    row_dict = dict()
    for x, y in dot_list:
        if y not in row_dict:
            row_dict[y] = [x]
        else:
            row_dict[y].append(x)

    couter_list = []
    for val in row_dict.values():
        temp = list(map(lambda x: (x[0], x[1]) if x[0] < x[1] else (
            x[1], x[0]), list(combinations(val, 2))))
        couter_list += temp

    count_square_dict = Counter(couter_list)

    result = 0
    for val in count_square_dict.values():
        if val >= 2:
            result += (val * (val - 1)) // 2

    print(result)

if __name__ == "__main__":
    solve1()
