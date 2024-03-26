# https://school.programmers.co.kr/learn/courses/30/lessons/86971 

def check(n, graph):
    from collections import deque

    visited = [0] * (n + 1)
    # bfs로 연결된 부분을 check하여서 temp에 연결된 부분의 수(cnt) 를 담아주고 return
    temp = []
    for i in range(1, n+1):
        if visited[i] == 0:
            queue = deque([i])
            visited[i] = 1
            cnt = 1
            while queue:
                cur_node = queue.popleft()
                for n_node in graph[cur_node]:
                    if visited[n_node] == 0:
                        queue.append(n_node)
                        visited[n_node] = 1
                        cnt += 1
            temp.append(cnt)
    return temp

def solution(n, wires):
    # 송전탑은 무조건 한번에 연결되어있다
    # n 이 100 이하 wires의 길이는 n보다 작으므로 bruteforce로 충분하다.

    result = float('inf')
    # 최솟값을 구하기 위해 최댓값을 설정한다

    from collections import defaultdict
    graph = defaultdict(list)
    # 그래프를 만들어준다
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)

    # 그래프에서 wires의 연결된 부분을 하나씩 잘라주면서 최솟값을 구해준다
    for s, e in wires:
        graph[s].remove(e)
        graph[e].remove(s)
        a, b = check(n, graph)
        result = min(result, abs(a-b))
        graph[s].append(e)
        graph[e].append(s)

    return result

