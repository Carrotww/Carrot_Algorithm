# https://www.acmicpc.net/problem/1916

def solve():
    import sys
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    bus_list = []
    
    for _ in range(M):
        bus_list.append(list(map(int, sys.stdin.readline().split())))
    
    start_city, end_city = map(int, sys.stdin.readline().split())