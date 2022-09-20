from collections import deque

balanced_parentheses_string = "()))((()"


def check_correct(string):
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(string[i])
        elif string[i] == ')':
            if not stack:
                return False
    if stack:
        return False
    else:
        return True
            
def 
def get_correct_parentheses(string):
    return


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!