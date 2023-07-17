# https://school.programmers.co.kr/learn/courses/30/lessons/176962

temp = "11:40"

print(temp.split(':'))

print(int(temp.split(':')[0])*60 + int(temp.split(':')[1]))

temp = [[x, y, z] for x, y, z in temp]