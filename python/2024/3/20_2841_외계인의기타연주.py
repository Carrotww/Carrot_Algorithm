# https://www.acmicpc.net/problem/2841

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, p = map(int, input().split())
    graph = [[] for _ in range(7)]

    result = 0
    for i in range(n):
        line, melody = map(int, input().split())
        if not graph[line]:
            result += 1
            graph[line].append(melody)
        else:
            if graph[line][-1] == melody:
                continue
            elif graph[line][-1] < melody:
                result += 1
                graph[line].append(melody)
            else:
                while graph[line] and graph[line][-1] > melody:
                    result += 1
                    graph[line].pop()
                if not graph[line]:
                    result += 1
                    graph[line].append(melody)
                elif graph[line][-1] == melody:
                    continue
                else:
                    graph[line].append(melody)
                    result += 1
    print(result)

