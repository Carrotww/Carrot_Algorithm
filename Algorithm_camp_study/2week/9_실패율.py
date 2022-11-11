def solution(N, stages):
    from collections import Counter
    temp = Counter(stages)
    result = []
    temp_len = 0
    for key, val in temp.items():
        if key > N:
            temp_len += val
    for i in range(N, 0, -1):
        if temp_len == 0:
            temp_len += temp[i]
            result.append((i, 0))
            continue
        result.append((i, temp[i] / (temp_len + temp[i])))
        temp_len += temp[i]

    return [x[0] for x in sorted(result, key=lambda x: x[1], reverse=True)]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
print(solution(8, [1, 2, 3, 4, 5, 6, 7]))