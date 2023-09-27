# https://www.acmicpc.net/problem/8980

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    city, truck = map(int, input().split())
    box_list = []
    for _ in range(int(input())):
        start, end, cost = map(int, input().split())
        box_list.append((start, end, cost))
    
    box_list.sort(key=lambda x:x[1])
    
    result = 0
    full = [truck] * (city + 1)
    for start, end, cost in box_list:
        min_val = truck
        for i in range(start, end):
            min_val = min(min_val, full[i])
        min_val = min(min_val, cost)
        
        for i in range(start, end):
            full[i] -= min_val
        result += min_val
    print(result)