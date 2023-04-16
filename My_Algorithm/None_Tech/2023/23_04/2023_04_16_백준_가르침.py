# https://www.acmicpc.net/problem/1062

def solve():
    import sys
    N, K = map(int, sys.stdin.readline().split())
    result = 0
    
    alpa = {'a', 'n', 't', 'i', 'c'}

    total_need_alpa = {}
    alpa_list = []

    for i in range(N):
        split_alpa = sys.stdin.readline().strip()[4:-4]
        alpa_list.append(split_alpa)
        need_alpa = set()
        for cur_alpa in split_alpa:
            if cur_alpa not in alpa:
                need_alpa.add(cur_alpa)
        if not need_alpa:
            continue
        need_alpa = ''.join(list(need_alpa))
        if need_alpa in total_need_alpa:
            total_need_alpa[need_alpa] += 1
        else:
            total_need_alpa[need_alpa] = 1

    if K < 5:
        print(result)
        return
    
    sorted_total_need_alpa = sorted(total_need_alpa.items(), key=lambda x: (x[0], x[1]), reverse=True)
    # print(sorted_total_need_alpa)

    cnt = 0
    for val, idx in sorted_total_need_alpa:
        for v in val:
            if cnt == K - 5:
                break
            if v not in alpa:
                alpa.add(v)
                cnt += 1
    
    for cur_word in alpa_list:
        is_add = True
        for cur_alpa in cur_word:
            if cur_alpa not in alpa:
                is_add = False
        if is_add:
            result += 1
    
    print(result)
    return

if __name__ == "__main__":
    solve()
# 6 6
# antabcdefgtica
# antabcdefgtica
# antabcdefgtica
# antabcdefgtica
# antabcdefgtica
# antaztica
'''
6 6
antarctica
antahellotica
antazzztica
antazzztica
antazzztica
antazzztica
'''