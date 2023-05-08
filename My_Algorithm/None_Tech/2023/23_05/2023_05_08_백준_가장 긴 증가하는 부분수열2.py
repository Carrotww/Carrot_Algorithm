# https://www.acmicpc.net/problem/12015

def solve():
    import sys
    N = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    LIS = [array[0]]

    for val in array:
        if LIS[-1] < val:
            LIS.append(val)
        else:
            left = 0
            right = len(LIS)

            while left < right:
                mid = (right + left) // 2
                if LIS[mid] < val:
                    left = mid + 1
                else:
                    right = mid
            LIS[right] = val
    
    print(len(LIS))

if __name__ == "__main__":
    solve()