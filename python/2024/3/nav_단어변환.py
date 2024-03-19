# https://school.programmers.co.kr/learn/courses/30/lessons/43163

def check(word1, word2):
    cnt = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            cnt += 1
            if cnt > 1:
                return False
        else:
            continue
    return True

def solution(begin, target, words):
    visited = [0] * len(words)

    def dfs(cur_word, cnt):
        if cur_word == target:
            return cnt
        min_cnt = float('inf')
        for i in range(len(words)):
            if not visited[i] and check(cur_word, words[i]):
                visited[i] = 1
                min_cnt = min(dfs(words[i], cnt+1), min_cnt)
                visited[i] = 0
        return min_cnt
    answer = dfs(begin, 0)
    if answer == float('inf'):
        return 0
    return answer

