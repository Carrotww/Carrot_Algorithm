# https://school.programmers.co.kr/learn/courses/30/lessons/172927

def solution(picks, minerals):
    result = 0
    
    minerals = minerals[:sum(picks)*5]
    slice_min = []
    
    def count_mineral(min_list):
        result = 0
        check_dict = {"diamond" : 15, "iron" : 5, "stone" : 1}
        for val in min_list:
            result += check_dict[val]
        
        return result
    
    cnt = 0
    tmp = []
    for mine in minerals:
        tmp.append(mine)
        cnt += 1
        if cnt == 5:
            weight = count_mineral(tmp)
            slice_min.append([weight, tmp])
            tmp = []
            cnt = 0
    
    if tmp:
        weight = count_mineral(tmp)
        slice_min.append([weight, tmp])
    
    slice_min.sort(key=lambda x:x[0])
    
    iron_graph = {"diamond" : 5, "iron" : 1, "stone" : 1}
    stone_graph = {"diamond" : 25, "iron" : 5, "stone" : 1}
    
    for i in range(3):
        for x in range(picks[i]):
            if slice_min:
                if i == 0:
                    mineral_list = slice_min.pop()[1]
                    result += len(mineral_list)
                elif i == 1:
                    mineral_list = slice_min.pop()[1]
                    for mineral in mineral_list:
                        result += iron_graph[mineral]
                else:
                    mineral_list = slice_min.pop()[1]
                    for mineral in mineral_list:
                        result += stone_graph[mineral]
            else:
                return result
    
    return result