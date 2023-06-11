# https://www.acmicpc.net/problem/18869

def solve():
    import sys
    from collections import defaultdict
    M, N = map(int, sys.stdin.readline().split())
    universe = []
    # for _ in range(M):
    #     temp = list(map(int, sys.stdin.readline().split()))
    #     temp = [(idx, val) for idx, val in enumerate(temp)]
    #     temp.sort(key=lambda x:x[1])
    #     temp = [idx for idx, val in temp]
    #     universe.append(','.join(map(str, temp)))
    
    uni_dict = defaultdict(int)
    for _ in range(M):
        temp = list(map(int, sys.stdin.readline().split()))
        s_temp = sorted(set(temp))
        temp_dict = dict()
        str_uni = ''
        for i in range(len(s_temp)):
            temp_dict[s_temp[i]] = i
        for te in temp:
            str_uni += str(temp_dict[te])
        uni_dict[str_uni] += 1
    
    result = 0
    for i in uni_dict.values():
        result += (i * (i - 1)) // 2
    
    print(result)

if __name__ == "__main__":
    solve()