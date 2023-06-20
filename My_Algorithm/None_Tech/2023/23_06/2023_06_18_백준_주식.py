# https://www.acmicpc.net/problem/11501

def solve():
    import sys
    day = int(sys.stdin.readline())
    stock_list = list(map(int, sys.stdin.readline().split()))

    max_stock = 0
    total_stock = 0
    
    for idx, val in enumerate(reversed(stock_list)):
        if val > max_stock:
            max_stock = val
        else:
            total_stock += (max_stock - val)
    
    print(total_stock)

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline())
    for _ in range(N):
        solve()
