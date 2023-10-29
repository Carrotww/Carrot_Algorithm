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

def solve():
    import sys
    N = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))

    LIS = [array[0]]
    positions = [0]
    parent = [-1] * N

    def findidx(value):
        left = 0
        right = len(LIS) - 1

        while left <= right:
            mid = (left + right) // 2
            if LIS[mid] < value:
                left = mid + 1
            else:
                right = mid - 1

        return left

    for i, val in enumerate(array[1:], 1):
        if LIS[-1] < val:
            parent[i] = positions[-1]
            LIS.append(val)
            positions.append(i)
        else:
            idx = findidx(val)
            LIS[idx] = val
            positions[idx] = i
            if idx > 0:
                parent[i] = positions[idx - 1]

    sequence = []
    index = positions[-1]
    while index != -1:
        sequence.append(array[index])
        index = parent[index]
    sequence.reverse()

    print(len(LIS))
    print(" ".join(map(str, sequence)))

if __name__ == "__main__":
    solve()