# https://school.programmers.co.kr/learn/courses/30/lessons/42626

def solution(sco, K):
    import heapq
    result = 0
    heapq.heapify(sco)

    while sco and (len(sco) > 1 or sco[0] < K):
        cur_food = heapq.heappop(sco)
        if cur_food >= K:
            break
        if not sco:
            # 이 부분이 원래 break였는데
            # 테케 3개정도 실패함 이유는 스코빌 지수 낮은걸 빼버리고 break로 탈출해서 그런듯
            # 처음 food를 빼고 여기 도달했다는 것은 처음 뺀 음식이 K 보다 작기 때문 그래서 그냥 return 해도 됨
            return -1
        n_food = heapq.heappop(sco)
        heapq.heappush(sco, cur_food + n_food * 2)
        result += 1
    if sco and sco[0] < K:
        return -1
    return result

    # 예외를 찾는데 좀 걸렸다 ㅠ 30분 정도 소요

