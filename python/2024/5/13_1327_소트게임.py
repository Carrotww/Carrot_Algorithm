# https://www.acmicpc.net/problem/1327

def swap(ary, index, k):
    return ary[:index] + ary[index:index+k][::-1] + ary[index+k:]

if __name__ == "__main__":
    from collections import deque
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().split())
    ary = list(map(int, input().split()))
    visited = set()
    visited.add(''.join(map(str, ary)))
    target = sorted(ary)

    result = -1
    queue = deque([[0, ary]])

    while queue:
        cur_cnt, cur_ary = queue.popleft()
        if cur_ary == target:
            result = cur_cnt
            break
        for i in range(n-k+1):
            new_ary = swap(cur_ary, i, k)
            new_ary_str = ''.join(map(str, new_ary))
            if new_ary_str in visited:
                continue
            visited.add(new_ary_str)
            queue.append([cur_cnt+1, new_ary])

    print(result)

