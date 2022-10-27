from collections import deque

def solution(begin, target, words):
    
    queue = deque([(begin, 0)])
    visited = [begin]
    while queue:
        temp_val, cnt = queue.popleft()
        if temp_val == target:
            return cnt
        for wo in words:
            diff_cnt = 0
            for i in range(len(wo)):
                if wo[i] != temp_val[i]:
                    diff_cnt += 1
                if diff_cnt > 1:
                    break
            if diff_cnt == 1 and wo not in visited:
                queue.append((wo, cnt+1))
                visited.append(wo)
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))