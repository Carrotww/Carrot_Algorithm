# https://school.programmers.co.kr/learn/courses/30/lessons/133500
from collections import defaultdict

def solution(n, lighthouse):
    path_dict = defaultdict(list)
    for a, b in lighthouse:
        path_dict[a].append(b)
        path_dict[b].append(a)
    
    path_list = sorted(path_dict.items(), key=lambda x:len(x[1]))

    path_list = [[x[0], x[1], len(x[1])] for x in path_list]

    cnt = 0

    while path_list:
        pop_n, pop_path, pop_cnt = path_list.pop()
        cnt += 1
        for x in range(len(path_list)):
            if path_list[x][2] != 0 and pop_n in path_list[x][1]:
                path_list[x][2] -= 1
        
        if sum([x[2] for x in path_list]) == 0:
            break

        path_list.sort(key=lambda x:x[2])

    return cnt

print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))