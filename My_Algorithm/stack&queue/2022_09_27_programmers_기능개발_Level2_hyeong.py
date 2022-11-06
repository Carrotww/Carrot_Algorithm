import math

def solution(progresses, speeds):
    stack = []
    for pro, sp in zip(progresses, speeds):
        temp = math.ceil((100 - pro) / sp)
        if not stack or stack[-1][0] < temp:
            stack.append([temp, 1])
            continue
        stack[-1][1] += 1
            
    return [x[1] for x in stack]

pro1, sp1 = [93, 30, 55], [1, 30, 5]
pro2, sp2 = [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]

print(solution(pro1, sp1))
print(solution(pro2, sp2))