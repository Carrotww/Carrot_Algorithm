# https://school.programmers.co.kr/learn/courses/30/lessons/43163

def check(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
            if cnt > 1:
                return False
    return True

# 지금 단어 word 와 main 함수에서 주어진 변수들 + visited를 받아서
def dfs(word, words, target, cnt, visited):
    if word == target:
        return cnt
    min_cnt = float('inf')
    for i in range(len(words)):
        if visited[i] == 0 and check(word, words[i]):
            visited[i] = 1
            temp = dfs(words[i], words, target, cnt+1, visited)
            min_cnt = min(min_cnt, temp)
            # min_cnt 에 최솟값을 넣어주고 visited에 나온 값을 방문 해제 시켜줌
            visited[i] = 0
    return min_cnt


def solution(begin, target, words):
    answer = 0
    # word 개수가 50개 이하이므로 전부 탐색하면 됨
    # dfs로 하면 될 것 같다고 생각함
    visited = [0] * len(words)

    result = dfs(begin, words, target, 0, visited)
    if result == float('inf'):
        return 0
    return result

