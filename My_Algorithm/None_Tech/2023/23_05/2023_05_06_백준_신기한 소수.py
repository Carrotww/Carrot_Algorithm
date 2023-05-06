# https://www.acmicpc.net/problem/2023

def solve():
    import sys
    N = int(sys.stdin.readline())

    def check(num):
        
        return True
    
    start, end = '', ''
    
    for i in range(N):
        if i == 0:
            start += '1'
            end += '9'
        else:
            start += '0'
            end += '9'
    
    start, end = int(start), int(end)
    result = []
    
    for i in range(start, end+1):
        if check(i):
            result.append(i)

if __name__ == "__main__":
    solve()