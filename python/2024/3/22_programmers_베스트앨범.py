# https://school.programmers.co.kr/learn/courses/30/lessons/42579 

def solution(genres, plays):
    result = []
    g_dict = {}
    # {'classic': 1450, 'pop': 3100}
    lank_dict = {}
    # {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]}
    for i in range(len(genres)):
        if genres[i] in g_dict:
            g_dict[genres[i]] += plays[i]
            lank_dict[genres[i]].append((plays[i], i))
        else:
            g_dict[genres[i]] = plays[i]
            lank_dict[genres[i]] = [(plays[i], i)]

    for g, total in sorted(g_dict.items(), key=lambda x:-x[1]):
        # pop 3100 -> classic 1450 순으로 정렬
        lank_dict[g].sort(key=lambda x:-x[0])

        # 각 장르에 곡이 하나인 경우가 있을 수 있음
        result.append(lank_dict[g][0][1])
        if len(lank_dict[g]) >= 2:
            result.append(lank_dict[g][1][1])

    # 총 정리 : 3레벨 맞음? python으로 하니 쉬운건가
    return result

