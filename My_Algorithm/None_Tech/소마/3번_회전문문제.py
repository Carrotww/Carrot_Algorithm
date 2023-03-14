'''
2* n 개의 칸으로 이루어진 회전문이 있으며 (0~ 2n-1까지 칸 번호 존재)
사람이 회전문에 진입하면 회전문은 진입한 순간부터 k초간 움직인다.

회전문은 1초에 1칸 반시계 방향으로 회전하며, 
동작중에 들어온 사람에 의해 회전문의 동작시간이 연장되지 않는다.

건물에 들어가는 사람은 0번으로, 건물에서 나오는 사람은 n번칸으로 진입한다.
다시말해 건물을 들어가고 빠져나가는데 걸리는 시간은 n초이다.

입력으로 사람이 나가는지, 들어오는지
몇 초에 회전문에 진입하였는지,
회전문은 총 몇칸으로 이루어져 있는지,
한번 동작을 시작한 회전문이 몇 초 동안 돌아가는지에 관한 정보가 주어질 때
각 사람이 회전문에서 빠져나오는 시간을 리스트에 담아 반환하라.
(빠져나올 수 없는 경우 -1을 넣으면 된다)

입력으로 동시에 같은 입구로 들어가는 상황은 주어지지 않는다.

만약 회전문에서 이동 중 회전문의 동작시간이 끝나
회전문에서 갇힌다면, 다음 사람이 들어올 때까지 회전문안에서 기다려야 한다.

0 < n <= k

return -> 각 사람이 빠져나올때까지 총 걸리는 시간 -> ex) [4, 8, 12, 20, -1, -1]
'''

from typing import List

def solution(k: int, n: int, people: List) -> List:
    # people -> [[0, 1], [0, 3], [1, 10], [1, 15]]
    result = []
    need_time = n
    # 현재 시간
    cur_time = 0
    # 회전문이 끝나는 시간
    left_turn_time = people[0][1] + k
    # result[0] -> 회전문 탈출에 남은 시간, result[1] -> 탈출한 시간, -1
    result.append([0, people[0][1] + need_time])

    for i in range(1, len(people)):
        # 사람이 입장한 시간에 회전문이 돌고있지 않으면
        cur_time = people[i][1]

        if left_turn_time <= cur_time:
            left_turn_time = cur_time + k
            # 전 사람이 탈출하지 못했다면
            cnt = i-1
            while result[cnt][1] == -1:
                result[cnt][1] = result[cnt][0] + cur_time
                cnt -= 1
                
            result.append([0, cur_time + need_time])
        
        elif left_turn_time >= cur_time + need_time:
            result.append([0, cur_time + need_time])
        
        elif left_turn_time < cur_time + need_time:
            result.append([need_time - (left_turn_time - cur_time), -1])
    
    return [y for x, y in result]


print(solution(5, 4, [[0, 1], [0, 4], [1, 12]])) # [5, 14, 16]
print(solution(5, 4, [[0, 1], [0, 4], [1, 12], [0, 15]])) # [5, 14, 16, -1]
print(solution(20, 6, [[0 ,1], [0 ,2], [0 ,3], [1, 18], [0, 19], [0, 20]])) # [7, 8, 9, -1, -1, -1]
print(solution(10, 4, [[0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 11], [0, 12]]))  # [7,8,9,10,11,12,-1,-1]
print(solution(10, 4,[[0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 11], [0, 12], [1, 26]]))  # [7,8,9,10,11,12,28, 29, 30]


def sol(k: int, n: int, people: List) -> List:
    result = [-1 for _ in range(len(people))]
    # people: 0/1, 진입시간
    people = [p[1] for p in people]
    people_len = len(people)
    remain = [n for _ in range(people_len)]
    stop_time = -1
    curr_idx = 0
    while curr_idx < people_len:
        entry_time = people[curr_idx]
        if entry_time >= stop_time:
            stop_time = entry_time + k
            prev_idx = curr_idx - 1
            while prev_idx >= 0 and remain[prev_idx] > 0:
                people[prev_idx] = entry_time
                prev_idx -= 1
        while curr_idx < people_len and people[curr_idx] + remain[curr_idx] <= stop_time:
            result[curr_idx] = people[curr_idx] + remain[curr_idx]
            remain[curr_idx] = 0
            curr_idx += 1

        while curr_idx < people_len and people[curr_idx] < stop_time:
            remain[curr_idx] -= (stop_time - people[curr_idx])
            people[curr_idx] += (stop_time - people[curr_idx])
            curr_idx += 1

    for p_idx in range(people_len):
        if remain[p_idx] > 0 and people[p_idx] + remain[p_idx] <= stop_time:
                result[p_idx] = people[p_idx] + remain[p_idx]

    return result


print(sol(5, 4, [[0, 1], [0, 4], [1, 12]]))  # [5, 14, 16]
print(sol(5, 4, [[0, 1], [0, 4], [1, 12], [0, 15]]))  # [5, 14, 16, -1]
print(sol(20, 6, [[0, 1], [0, 2], [0, 3], [1, 18], [0, 19], [0, 20]]))  # [7, 8, 9, -1, -1, -1]
print(sol(10, 4, [[0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 11], [0, 12]]))  # [7,8,9,10,11,12,-1,-1]
print(sol(10, 4,[[0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 11], [0, 12], [1, 26]]))  # [7,8,9,10,11,12,28, 29, 30]