# https://www.acmicpc.net/problem/2504

def solve():
    import sys
    
    value = list(sys.stdin.readline().strip())
    stack = []
    result = 0
    temp = 1

    for i in range(len(value)):
        if value[i] == "(":
            stack.append(value[i])
            temp *= 2
        elif value[i] == "[":
            stack.append(value[i])
            temp *= 3
        else:
            if value[i] == ")":
                if not stack or stack[-1] == "[":
                    result = 0
                    break
                if value[i-1] == "(":
                    result += temp
                stack.pop()
                temp //= 2
            else:
                if not stack or stack[-1] == "(":
                    result = 0
                    break
                if value[i-1] == "[":
                    result += temp
                stack.pop()
                temp //= 3
    
    if stack:
        print(0)
    else:
        print(result)

if __name__ == "__main__":
    solve()