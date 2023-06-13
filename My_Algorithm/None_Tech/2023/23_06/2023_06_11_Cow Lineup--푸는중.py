# https://www.acmicpc.net/problem/5926

def solve():
    import sys
    from collections import defaultdict
    N = int(sys.stdin.readline())
    cow_list = []
    breed_set = set()

    for _ in range(N):
        x, breed = map(int, sys.stdin.readline().split())
        breed_set.add(breed)
        cow_list.append((x, breed))
    cow_list.sort()
    total_breed = len(breed_set)
    result = float('inf')

    for i in range(len(cow_list)):
        check_set = set()
        cnt = 0
        idx = i
        while idx < N:
            if cow_list[idx][1] not in check_set:
                check_set.add(cow_list[idx][1])
                cnt += 1
            if cnt == total_breed:
                result = min(result, cow_list[idx][0] - cow_list[i][0])
                break
            idx += 1
    
    print(result)

if __name__ == "__main__":
    solve()