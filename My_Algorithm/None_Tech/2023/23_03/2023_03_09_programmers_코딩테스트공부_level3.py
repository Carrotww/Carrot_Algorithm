# https://school.programmers.co.kr/learn/courses/30/lessons/118668

# 처음 풀이 풀다 포기 - brute force

def solution(alp, cop, problems):
    max_al_req, max_co_req = 0, 0
    min_al_req, min_co_req = 21, 21
    time = 0
    for al_q, co_q, al_r, co_r, cost in problems:
        max_al_req = max(max_al_req, al_q)
        max_co_req = max(max_co_req, co_q)
        min_al_req = min(min_al_req, al_q)
        min_co_req = min(min_co_req, co_q)
    
    need_al = max_al_req - alp
    need_co = max_co_req - cop
    
    def can_solve_problem(cur_alp, cur_cop):
        can_solve_problem_list = []
        for idx, val in problems:
            if cur_alp >= val[0] and cur_cop >= val[1]:
                can_solve_problem_list.append(idx)
        
        return can_solve_problem_list
    
    while alp < max_al_req or cop < max_co_req:
        can_solve_list = can_solve_problem(alp, cop)
        if len(can_solve_list) >= len(problems):
            return time
        
        need_al = max_al_req - alp
        need_co = max_co_req - cop
        
        if can_solve_list:
            pass
        else:
            pass

# 두 번째 풀이 dp

def solution(alp, cop, problems):
    
    return