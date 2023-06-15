# https://www.acmicpc.net/problem/1976

def solve():
    import sys
    from collections import defaultdict, deque

    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    graph = defaultdict(set)
    for i in range(1, n+1):
        city = 1
        for j in list(map(int, sys.stdin.readline().split())):
            if j == 1 or city == i:
                graph[i].add(city)
                graph[city].add(i)
            city += 1

    route = list(map(int, sys.stdin.readline().split()))
    check = set()
    queue = deque()
    queue.append(route[0])

    while queue:
        cur_city = queue.popleft()
        for n_city in graph[cur_city]:
            if (cur_city, n_city) not in check:
                check.add((cur_city, n_city))
                queue.append(n_city)

    check_city = set()
    for a, b in check:
        check_city.add(a)
        check_city.add(b)

    is_yes = True
    for r in route:
        if r not in check_city:
            is_yes = False
            break
    if is_yes:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    solve()
