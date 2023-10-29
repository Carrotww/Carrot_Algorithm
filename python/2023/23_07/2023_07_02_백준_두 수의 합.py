# https://www.acmicpc.net/problem/3273

def solve():
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    nums = list(map(int, input().split()))
    x = int(input())
    nums.sort()
    cnt = 0
    
    left, right = 0, n-1
    while left < right:
        total = nums[left] + nums[right]
        if total == x:
            left += 1
            cnt += 1
        elif total < x:
            left += 1
        else:
            right -= 1
    
    print(cnt)

def solve1():
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    nums = list(map(int, input().split()))
    x = int(input())
    nums.sort()
    cnt = 0
    
    right = n-1
    for start in range(n-1):
        while start < right:
            total = nums[start] + nums[right]
            if total == x:
                cnt += 1
                break
            elif total < x:
                break
            else:
                right -= 1
    print(cnt)
                
    
if __name__ == "__main__":
    solve1()


