# https://www.acmicpc.net/problem/15686

if __name__ == "__main__":
    import sys
    from itertools import combinations

    input = sys.stdin.readline
    
    n, m = map(int, input().split())

    graph = []
    chicken_list = []
    home_list = []

    for r in range(n):
        temp = list(map(int, input().split()))
        graph.append(temp)
        for c in range(n):
            if temp[c] == 2:
                chicken_list.append([r, c])
            elif temp[c] == 1:
                home_list.append([r, c])
    
    result = float('inf')
    for t_chicken_list in combinations(chicken_list, m):
        temp = 0
        for home in home_list:
            min_dis = float('inf')
            h_r, h_c = home
            for chicken in t_chicken_list:
                c_r, c_c = chicken
                min_dis = min(min_dis, abs(h_r-c_r) + abs(h_c-c_c))
            temp += min_dis
        result = min(temp, result)
    
    print(result)