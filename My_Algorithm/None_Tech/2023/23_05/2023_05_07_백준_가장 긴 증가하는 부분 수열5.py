# https://www.acmicpc.net/problem/14003

def solve():
    import sys
    N = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))

    LIS = [array[0]]

    for val in array:
        if LIS[-1] < val:
            LIS.append(val)
        else:
            left, right = 0, len(LIS)
            
            while left < right:
                mid = (left + right) // 2
                if LIS[mid] < val:
                    left = mid + 1
                else:
                    right = mid
            LIS[left] = val
    
    print(len(LIS))
    print(' '.join([str(x) for x in LIS]))

if __name__ == "__main__":
    solve()