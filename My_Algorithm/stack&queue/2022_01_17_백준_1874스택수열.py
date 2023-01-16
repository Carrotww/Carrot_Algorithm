# https://www.acmicpc.net/problem/1874

import sys
n = int(sys.stdin.readline())

def Solution(n):
    stack, result = [], []
    cnt = 1
    for i in range(n):
        num = int(sys.stdin.readline())
        while cnt <= num:
            stack.append(cnt)
            result.append('+')
            cnt += 1
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            return False
    return result

result = Solution(n)

if result:
    for i in result:
        print(i)
else:
    print('NO')