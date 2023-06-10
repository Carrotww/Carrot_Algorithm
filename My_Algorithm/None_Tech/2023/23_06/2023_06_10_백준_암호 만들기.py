# https://www.acmicpc.net/problem/1759

def solve():
    import sys
    
    l, c = map(int, sys.stdin.readline().split())
    words = list(sys.stdin.readline().split())
    words.sort()

    def check(ary):
        temp = [0, 0]
        for a in ary:
            if a in {'a', 'e', 'i', 'o', 'u'}:
                temp[0] += 1
            else:
                temp[1] += 1
        return temp

    result = []
    def dfs(ary, cnt, idx):
        if cnt == l:
            check_cnt = check(ary)
            if check_cnt[0] >= 1 and check_cnt[1] >= 2:
                result.append(ary[:])
                return
            return
        for i in range(idx, c):
            ary.append(words[i])
            dfs(ary, cnt+1, i+1)
            ary.pop()
    
    dfs([], 0, 0)
    
    for re in result:
        print(''.join(re))

if __name__ == "__main__":
    solve()