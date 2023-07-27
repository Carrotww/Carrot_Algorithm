# https://school.programmers.co.kr/learn/courses/30/lessons/150367

def check_binary_tree(tree):
    if len(tree) == 1 or '1' not in tree or '0' not in tree:
        return True
    mid = len(tree) // 2
    if tree[mid] == '0':
        return False

    return check_binary_tree(tree[:mid]) and check_binary_tree(tree[mid+1:])


def solution(numbers):
    result = []
    for num in numbers:
        b = bin(num)[2:]
        bb = bin(len(b) + 1)[2:]
        cur_result = 0
        if '1' in bb[1:]:
            diff = int('0b1' + '0' * len(bb), 2) - int('0b' + bb, 2)
            b = diff * '0' + b
        if check_binary_tree(b):
            cur_result = 1
        result.append(cur_result)

    return result