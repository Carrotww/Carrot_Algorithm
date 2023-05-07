# https://www.acmicpc.net/problem/2023

def solve():
    import sys
    N = int(sys.stdin.readline())

    def check(num):
        if num == 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        
        return True
    
    def dfs(num):
        if len(str(num)) == N:
            print(num)
        else:
            for i in range(10):
                temp = num*10+i
                if check(temp):
                    dfs(temp)
    
    dfs(2)
    dfs(3)
    dfs(5)
    dfs(7)

if __name__ == "__main__":
    solve()