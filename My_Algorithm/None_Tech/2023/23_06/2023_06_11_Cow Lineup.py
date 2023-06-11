# https://www.acmicpc.net/problem/5926

def solve():
    import sys
    N = int(sys.stdin.readline())
    cow_list = []
    breed_set = set()

    for _ in range(N):
        x, breed = map(int, sys.stdin.readline().split())
        breed_set.add(breed)
        cow_list.append((x, breed))
    cow_list.sort()
    check_breed = set()
    start, end = 0, 0
    if len(breed_set) == 1:
        print(1)
        return

    for x, breed in cow_list:
        check_breed.add(breed)
        if len(check_breed) == len(breed_set):
            end = x
            break

    check_cnt = len(check_breed)
    for x, breed in reversed(cow_list):
        if breed in check_breed:
            check_breed.remove(breed)
            check_cnt -= 1
            if check_cnt == 0:
                start = x
                break

    print(end - start + 1)

if __name__ == "__main__":
    solve()
