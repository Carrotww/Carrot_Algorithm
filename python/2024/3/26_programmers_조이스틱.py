# https://school.programmers.co.kr/learn/courses/30/lessons/42860 

def solution(name):
    move_idx = len(name) - 1
    change_idx = 0

    for i in range(len(name)):
        change_idx += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1

        # 1. 쭉 가는 방법
        # 2. BBBAAAAAAAAAB 상황에서 0번 인덱스에서 맨 오른쪽 부터 찍고 오는 경우
        # 3. BBBAAAAAAAAAAAAAAAAABBBBB 상황에서 왼쪽의 B를 처리하고 돌아가서 B를 처리하는 경우
        move_idx = min(move_idx, i + 2*(len(name)-next_idx), i + i + len(name) - next_idx)

    return move_idx + change_idx

