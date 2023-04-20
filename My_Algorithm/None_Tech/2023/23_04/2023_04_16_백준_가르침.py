# https://www.acmicpc.net/problem/1062

# def solve():
#     import sys
#     N, K = map(int, sys.stdin.readline().split())
#     result = 0
    
#     alpa = {'a', 'n', 't', 'i', 'c'}

#     total_need_alpa = {}
#     alpa_list = []

#     for i in range(N):
#         split_alpa = sys.stdin.readline().strip()[4:-4]
#         alpa_list.append(split_alpa)
#         need_alpa = set()
#         for cur_alpa in split_alpa:
#             if cur_alpa not in alpa:
#                 need_alpa.add(cur_alpa)
#         if not need_alpa:
#             continue
#         need_alpa = ''.join(list(need_alpa))
#         if need_alpa in total_need_alpa:
#             total_need_alpa[need_alpa] += 1
#         else:
#             total_need_alpa[need_alpa] = 1

#     if K < 5:
#         print(result)
#         return
    
#     sorted_total_need_alpa = sorted(total_need_alpa.items(), key=lambda x: (x[0], x[1]), reverse=True)
#     # print(sorted_total_need_alpa)

#     cnt = 0
#     for val, idx in sorted_total_need_alpa:
#         for v in val:
#             if cnt == K - 5:
#                 break
#             if v not in alpa:
#                 alpa.add(v)
#                 cnt += 1
    
#     for cur_word in alpa_list:
#         is_add = True
#         for cur_alpa in cur_word:
#             if cur_alpa not in alpa:
#                 is_add = False
#         if is_add:
#             result += 1
    
#     print(result)
#     return

# def solve2():
#     from itertools import combinations
#     import sys
#     N, K = map(int, sys.stdin.readline().split())
#     word_list = [sys.stdin.readline().strip()[4:-4] for _ in range(N)]
#     base_char = {'a', 'n', 't', 'i', 'c'}

#     visited = set([])

#     for word in word_list:
#         for char in word:
#             if char not in base_char:
#                 visited.add(char)
    
#     visited = list(visited)
#     result = 0
    
#     if K < 5:
#         print(result)
#     else:
#         K -= 5
#         if K > len(visited):
#             K = len(visited)
        
#         for com in combinations(visited, K):
#             cnt = 0
#             for word in word_list:
#                 for w in word:
#                     if w not in base_char and w not in com:
#                         break
#                 else:
#                     cnt += 1
#             result = max(result, cnt)
#         print(result)
    
def solve3():
    import sys
    N, K = map(int, sys.stdin.readline().split())
    # word_list = [set(sys.stdin.readline().strip()[4:-4]) for _ in range(N)]
    word_list = [sys.stdin.readline().strip() for _ in range(N)]
    alph = [0] * 26

    def dfs(idx, cnt):
        nonlocal result
        if K - 5 == cnt:
            read_cnt = 0
            for word in word_list:
                is_read = True
                for w in word:
                    if alph[ord(w) - ord('a')] == 0:
                        is_read = False
                        break
                if is_read:
                    read_cnt += 1
            result = max(result, read_cnt)

            # return
        
        for i in range(idx, 26):
            if alph[i] == 0:
                alph[i] = 1
                dfs(i, cnt+1)
                alph[i] = 0

    if K < 5:
        print(0)
    else:
        for char in ('a', 'c', 'i', 'n', 't'):
            alph[ord(char) - ord('a')] = 1
        
        result = 0
        dfs(0, 0)
        print(result)

if __name__ == "__main__":
    # solve()
    # solve2()
    solve3()

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