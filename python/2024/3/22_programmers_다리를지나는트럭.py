# https://school.programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    # 최대 만개의 트럭이 만 kg 이여도 만 길이의 다리를 통과하는데 10000 * 10000 밖에 안걸림

    from collections import deque

    bridge = deque()
    # 다리를 나타내는 큐
    truck_weights = deque(truck_weights)
    total = 0
    # 다리에 올라온 트럭의 무게를 재는 변수

    time = 1
    # 다리에 여유가 있다면 트럭을 올리고
    # 트럭이 나올시간이 되었으면 트럭을 bridge에서 빼준다
    # 트럭이 bridge에서 나오면서 total 에서 무게를 빼줘야함
    while truck_weights:
        if bridge and bridge[0][0] <= time:
            # 다리에 빠져나올시간이 된 트럭 빼줌
            total -= bridge[0][1]
            # 빼준 트럭의 무게를 다리의 총 무게에서 빼줌
            bridge.popleft()
        if truck_weights[0] + total <= weight:
            # 다리에 트럭 넣을 수 있으면 넣어줌
            bridge.append([time+bridge_length, truck_weights[0]])
            # bridge -> ["나올시간", "해당트럭무게"]
            total += truck_weights[0]
            # 다리 총 무게에 트럭 무게 추가
            truck_weights.popleft()
        time += 1

    return bridge[-1][0]

    # 후기 : 집중해서 풀면 된다 약 15분
