# https://www.acmicpc.net/problem/5926

def solve():
    import sys
    from collections import defaultdict
    N = int(sys.stdin.readline())
    cow_list = []
    breed_dict = defaultdict(int)
    breed_set = set()

    for _ in range(N):
        x, breed = map(int, sys.stdin.readline().split())
        breed_set.add(breed)
        cow_list.append([x, breed])

    # [15, 1] [20, 1] [22, 3] [25, 7] [26, 1]
    total = len(breed_set)
    breed_set = set()
    cow_list.sort()
    start, end = 0, 0
    result = float('inf')

    while end < N:
        cur_x, cur_breed = cow_list[end]
        breed_set.add(cur_breed)
        breed_dict[cur_breed] += 1

        while len(breed_set) == total:
            result = min(result, cur_x - cow_list[start][0])
            breed_dict[cow_list[start][1]] -= 1
            if breed_dict[cow_list[start][1]] == 0:
                breed_set.remove(cow_list[start][1])
            start += 1
        end += 1

    print(result)


if __name__ == "__main__":
    solve()
