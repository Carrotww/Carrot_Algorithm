# https://www.acmicpc.net/problem/15591

def solution(k, node):
    temp_list = []
    for i in graph[node]:
        temp_list.append(i)

    next_list = temp_list[::]
    
    for end_node, cur_weight in temp_list:
        for next_end_node, next_weight in graph[end_node]:
            if next_end_node == node:
                continue
            next_list.append([next_end_node, min(cur_weight, next_weight)])
    
    cnt = 0
    for end_node, cur_weight in next_list:
        if cur_weight >= k:
            cnt += 1
    return cnt

if __name__ == "__main__":
    import sys
    from collections import defaultdict
    result = []
    graph = defaultdict(list)
    n, q = map(int, sys.stdin.readline().split())

    for _ in range(n-1):
        start, end, weight = map(int, sys.stdin.readline().split())
        graph[start].append([end, weight])
        graph[end].append([start, weight])
    
    for _ in range(q):
        k, node = map(int, sys.stdin.readline().split())
        result.append(solution(k, node))
    
    for re in result:
        print(re)