def solve():
    import sys

    result = []
    while 1:
        cur_val = sys.stdin.readline().strip()
        if cur_val[0] == '-':
            break
        else:
            cnt = 0
            stack = []
            for val in cur_val:
                if val == '{':
                    stack.append(val)
                elif val == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        stack.append('{')
                        cnt += 1
            cnt += len(stack) // 2
            result.append(cnt)
    
    for idx, val in enumerate(result):
        print(f'{idx+1}. {val}')

if __name__ == "__main__":
    solve()