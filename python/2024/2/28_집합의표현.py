# https://www.acmicpc.net/problem/1717

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(1000000)
    input = sys.stdin.readline

    n, m = map(int, input().split())
    result = []
    parent = [x for x in range(n+1)]

    for _ in range(m):
        num, a, b = map(int, input().split())
        if num == 0:
            union(a, b)
        else:
            ap, bp = find(a), find(b)
            if ap != bp:
                result.append("no")
            else:
                result.append("yes")
            

    for i in range(len(result)):
        print(result[i])

