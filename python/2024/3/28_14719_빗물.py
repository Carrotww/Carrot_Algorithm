# https://www.acmicpc.net/problem/14719

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    h, w = map(int, input().split())
    graph = list(map(int, input().split()))

    result = 0

    for i in range(1, w-1):
        left, right = max(graph[:i]), max(graph[i+1:])
        height = min(left, right)
        if height <= graph[i]:
            continue
        result += (height - graph[i])
    print(result)


# 두 번째 풀이
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    h, w = map(int, input().split())
    graph = list(map(int, input().split()))

    stack = []
    result = 0

    for i in range(w):
        while stack and graph[i] > graph[stack[-1]]:
            pre_idx = stack.pop()
            if not stack:
                break
            height = min(graph[stack[-1]], graph[i]) - graph[pre_idx]
            distance = i - stack[-1] - 1
            result += height * distance
        stack.append(i)
    print(result)

