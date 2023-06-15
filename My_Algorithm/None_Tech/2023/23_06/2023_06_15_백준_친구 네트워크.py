# https://www.acmicpc.net/problem/4195

def solve():
    import sys
    n = int(sys.stdin.readline())

    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    def union_parent(parent, count, x, y):
        x = find_parent(parent, x)
        y = find_parent(parent, y)
        if x != y:
            parent[y] = x
            count[x] += count[y]
    
    parent = dict()
    count = dict()
    
    for _ in range(n):
        x, y = sys.stdin.readline().split()
        
        if x not in parent:
            parent[x] = x
            count[x] = 1
        
        if y not in parent:
            parent[y] = y
            count[y] = 1
        
        union_parent(parent, count, x, y)
        print(count[find_parent(parent, x)])

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline())
    for _ in range(N):
        solve()