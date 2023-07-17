# https://www.acmicpc.net/problem/1032

def solve():
    import sys
    from collections import defaultdict
    
    N = int(sys.stdin.readline())
    patterns = defaultdict(set)
    for _ in range(N):
        word = sys.stdin.readline().strip()
        for i in range(len(word)):
            patterns[i].add(word[i])

    for key, val in patterns.items():
        if len(val) > 1:
            result += '?'
        else:
            result += val.pop()
    
    print(''.join(result))

if __name__ == "__main__":
    solve()