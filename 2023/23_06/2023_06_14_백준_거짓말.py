# https://www.acmicpc.net/problem/1043

def solve():
    import sys
    from collections import defaultdict, deque
    N, M = map(int, sys.stdin.readline().split())
    know_people = list(map(int, sys.stdin.readline().split()))
    if know_people[0] == 0:
        print(M)
        return
    else:
        know_people = know_people[1::]
    graph = defaultdict(list)
    party = dict()

    for party_num in range(1, M+1):
        cur_party = list(map(int, sys.stdin.readline().split()))
        party_people_list = cur_party[1::]
        party[party_num] = party_people_list
        for people in party_people_list:
            graph[people].append(party_num)

    visited = [False for _ in range(N+1)]
    queue = deque()
    for people in know_people:
        queue.append(people)

    while queue:
        cur_people = queue.popleft()
        for party_num in graph[cur_people]:
            for people in party[party_num]:
                if visited[people]:
                    continue
                visited[people] = True
                queue.append(people)

    result = M
    for people_list in party.values():
        is_true = False
        for people in people_list:
            if visited[people]:
                is_true = True
                break
        if is_true:
            result -= 1

    print(result)

if __name__ == "__main__":
    solve()
