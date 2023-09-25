# https://www.acmicpc.net/problem/9370

def dj(node):
    heap = []
    heapq.heappush(heap, (0, node))
    visited = [float('inf')] * (n + 1)
    visited[node] = 0

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        if visited[cur_node] < cur_dist:
            continue
        for n_node, n_dist in graph[cur_node]:
            dist = cur_dist + n_dist
            if dist < visited[n_node]:
                visited[n_node] = dist
                heapq.heappush(heap, (dist, n_node))

    return visited


if __name__ == "__main__":
    import sys
    import heapq
    from collections import defaultdict

    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        n, m, t = map(int, input().split())
        s, g, h = map(int, input().split())
        graph = defaultdict(list)

        for _ in range(m):
            start, end, dist = map(int, input().split())
            graph[start].append((end, dist))
            graph[end].append((start, dist))

        result = []
        
        s_t = dj(s)
        g_t = dj(g)
        h_t = dj(h)
        gh_dist = g_t[h]
        start_to_g = s_t[g]
        start_to_h = s_t[h]

        for _ in range(t):
            target = int(input())

            start_to_target = s_t[target]
            g_to_target = g_t[target]
            h_to_target = h_t[target]

            if start_to_target == float('inf') or start_to_g == float('inf') \
                or h_to_target == float('inf') or g_to_target == float('inf'):
                    continue

            if start_to_target == start_to_g + h_to_target + gh_dist \
                    or start_to_target == start_to_h + g_to_target + gh_dist:
                result.append(target)

        result.sort()
        print(' '.join([str(x) for x in result]))