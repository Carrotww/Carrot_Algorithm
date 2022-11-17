# https://school.programmers.co.kr/learn/courses/30/lessons/132266

from collections import deque, defaultdict
import math

def solution(n, roads, sources, destination):
    roads_path = defaultdict(list)
    for a, b in roads:
        roads_path[a].append(b)
        roads_path[b].append(a)
    
    result = []
    for so in sources:
        queue = deque([so])
        visited = {x:math.inf for x in range(1, n + 1)}
        visited[so] = 0
        # x -> n ; value -> so 와의 거리
        while queue:
            if visited[destination] != math.inf:
                result.append(visited[destination])
                break
            cur_road = queue.popleft()
            cur_path = visited[cur_road]
            for next_road in roads_path[cur_road]:
                if visited[next_road] > cur_path + 1:
                    visited[next_road] = cur_path + 1
                    queue.append(next_road)
        if visited[destination] == math.inf:
            result.append(-1)
    return result