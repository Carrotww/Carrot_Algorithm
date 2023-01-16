import sys

temp = list(map(int, sys.stdin.readline().split()))[0]

def solution(temp: int) -> int:
    cnt = 0
    result = temp
    temp = str(temp)

    while 1:
        if len(temp) == 1:
            temp = '0' + temp
        
        first = temp[1]
        second = int(temp[0]) + int(temp[1])
        if len(str(second)) == 1:
            temp = first + str(second)
        else:
            temp = first + str(second)[1]
        cnt += 1

        if int(temp) == result:
            break

    return cnt

print(solution(temp))