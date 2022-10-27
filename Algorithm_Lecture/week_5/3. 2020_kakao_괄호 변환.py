from collections import deque

balanced_parentheses_string = "()))((()"

def check_correct(string):
    stack = []
    for st in string:
        if st == '(':
            stack.append(st)
        else:
            if not stack: return False
            stack.pop()
    if stack: return False
    else: return True

def check_uv(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = '', ''
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    v = ''.join(list(queue))
    return u, v

def change_correct(string):
    if string == '':
        return ''
    u, v = check_uv(string)
    if check_correct(u):
        return u + change_correct(v)
    else:
        return '(' + change_correct(v) + ')' + ''.join(list(map(lambda x:'(' if x==')' else ')', u[1:-1])))
    
def get_correct_parentheses(string):
    if check_correct(string):
        return string
    else:
        return change_correct(string)

print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!