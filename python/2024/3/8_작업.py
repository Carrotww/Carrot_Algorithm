# https://www.acmicpc.net/problem/2056

def topology_sort(node):
    from collections import deque
    queue = deque()
    
    max_val = 0
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append([i, spend_time[i]])
            max_val = max(max_val, spend_time[i])

    while queue:
        cur_node, cur_time = queue.popleft()
        max_val = max(max_val, cur_time)
        for n_node in graph[cur_node]:
            indegree[n_node] -= 1
            if indegree[n_node] == 0:
                queue.append([n_node, spend_time[n_node]+cur_time])
                print("n_node : ", n_node, " spend_time[n_node] : ", spend_time[n_node], " cur_time : ", cur_time, " max_val : ", max_val)
    return max_val

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n+1)]
    spend_time = [0] * (n + 1)

    for i in range(1, n+1):
        t = list(map(int, input().split()))
        spend_time[i] = t[0]
        for j in range(t[1]):
            indegree[i] += 1
            graph[t[j+2]].append(i)

    result = topology_sort(1)
    print(result)


