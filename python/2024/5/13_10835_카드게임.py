# https://www.acmicpc.net/problem/10835

def dfs(left_idx, right_idx, total):
    global result

    if left_idx == n or right_idx == n:
        result = max(result, total)
        return

    if right[right_idx] < left[left_idx]:
        dfs(left_idx, right_idx+1, right[right_idx]+total)
    else:
        dfs(left_idx+1, right_idx+1, total)
        dfs(left_idx+1, right_idx, total)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))

    result = 0
    
    dfs(0, 0, 0)

    print(result)

