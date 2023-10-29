# https://www.acmicpc.net/problem/2470

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    solid = list(map(int, input().split()))

    max_val = float('inf')
    solid.sort()
    start, end = 0, N-1
    result_s, result_e = 0, 0
    
    while start < end:
        val = solid[start] + solid[end]
        if max_val > abs(val):
            max_val = abs(val)
            result_s, result_e = start, end
        
        if val < 0:
            start += 1
        elif val > 0:
            end -= 1
        else:
            break
    print(solid[result_s], solid[result_e])