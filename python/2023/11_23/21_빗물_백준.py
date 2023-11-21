# https://www.acmicpc.net/problem/14719
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    h, w = map(int, input().split())
    ary = list(map(int, input().split()))

    stack = []
    result = 0
    for i in range(w):
        while stack and ary[i] > ary[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = (i - stack[-1] - 1)
            height = min(ary[i], ary[stack[-1]]) - ary[top]
            result += (distance * height)
        stack.append(i)
    print(result)
