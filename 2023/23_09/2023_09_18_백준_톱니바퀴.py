# https://www.acmicpc.net/problem/14891

def move(num, direct, before_val, next):
    if num+next < 0 or num+next >= 4:
        return
    
    cur_gear = gear[num+next]
    right_val = cur_gear[2]
    left_val = cur_gear[6]

    if next == 1 and before_val == gear[num+next][6]:
        return
        
    if next == -1 and before_val == gear[num+next][2]:
        return
    
    if direct == -1:
        front = cur_gear.popleft()
        cur_gear.append(front)
    else:
        back = cur_gear.pop()
        cur_gear.appendleft(back)
    gear[num+next] = cur_gear
    
    if next == 1:
        move(num+next, -direct, right_val, next)
    else:
        move(num+next, -direct, left_val, next)

if __name__ == "__main__":
    import sys
    from collections import deque

    input = sys.stdin.readline

    a = deque(list(map(int, input().rstrip())))
    b = deque(list(map(int, input().rstrip())))
    c = deque(list(map(int, input().rstrip())))
    d = deque(list(map(int, input().rstrip())))

    gear = [a, b, c, d]

    K = int(input())
    command = []
    for _ in range(K):
        command.append(list(map(int, input().split())))

    # 1 -> right -1 -> left
    for com in range(K):
        num, direct = command[com][0]-1, command[com][1]
        cur_gear = gear[num]
        right_val = cur_gear[2]
        left_val = cur_gear[6]

        if direct == -1:
            front = cur_gear.popleft()
            cur_gear.append(front)
            gear[num] = cur_gear
            move(num, -direct, right_val, 1)
            move(num, -direct, left_val, -1)
        else:
            back = cur_gear.pop()
            cur_gear.appendleft(back)
            gear[num] = cur_gear
            move(num, -direct, right_val, 1)
            move(num, -direct, left_val, -1)
    
    result = 0
    for i in range(4):
        if gear[i][0] == 1:
            result += (2 ** i)
    print(result)