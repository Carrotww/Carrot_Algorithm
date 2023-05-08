# https://www.acmicpc.net/problem/14003

def solve():
    import sys
    N = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))

    LIS = [array[0]]

    def findidx(value):
        start = 0
        end = len(LIS) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if LIS[mid] == value:
                return mid
            elif LIS[mid] < value:
                start = mid + 1
            else:
                end = mid
        
        return start
    
    for val in array:
        if LIS[-1] < val:
            LIS.append(val)
        else:
            idx = findidx(val)
            LIS[idx] = val
    
    print(len(LIS))

if __name__ == "__main__":
    solve()