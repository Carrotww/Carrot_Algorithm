# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    result = []
    
    for ar1, ar2 in zip(arr1, arr2):
        line1 = format(ar1, 'b')
        line2 = format(ar2, 'b')
        temp = int(line1) + int(line2)
        temp = str(temp)
        while len(temp) != n:
            temp = '0' + temp
        temp = temp.replace('0', ' ')
        temp = temp.replace('1', '#')
        temp = temp.replace('2', '#')
        result.append(temp)
    return result

"""
def solution(n, arr1, arr2):
    hint_map = []
    
    for ar1, ar2 in zip(arr1, arr2):
        line1 = format(ar1, 'b')
        line2 = format(ar2, 'b')
        temp = int(line1) + int(line2)
        temp = str(temp)
        while len(temp) != n:
            temp = '0' + temp
        hint_map.append(temp)
        
    result = []
    for hm in hint_map:
        temp = ''
        for h in hm:
            if h != '0':
                temp += '#'
            else:
                temp += ' '
        result.append(temp)
    return result
"""
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))