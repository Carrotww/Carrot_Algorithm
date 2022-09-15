s = "(())()"


def is_correct_parenthesis(string):
    temp = []
    for i in range(len(string)):
        if string[i] == '(':
            temp.append(i)
        elif string[i] == ')':
            if not temp:
                return False
            temp.pop()
    if temp:
        return False
    else:
        return True

print(is_correct_parenthesis("(())"))
print(is_correct_parenthesis(")"))
print(is_correct_parenthesis("((())))"))
print(is_correct_parenthesis("())()"))
print(is_correct_parenthesis("((())"))