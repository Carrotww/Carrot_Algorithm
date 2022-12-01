# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    result = []
    
    temp = []
    
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            temp.append(dartResult[i:i+2])
        elif not (dartResult[i].isdigit() or dartResult[i].isalpha()):
            temp.append(dartResult[i])
            
    for i in temp:
        if len(i) == 2:
            if i[1] == 'S':
                result.append(int(i[0]))
            elif i[1] == 'D':
                result.append(int(i[0]) ** 2)
            elif i[1] == 'T':
                result.append(int(i[0]) ** 3)
        else:
            if i == '*':
                result[-1] = result[-1] * 2
            else:
                result[-1] = result[-1] * -1
    print(result)
    return sum(result)