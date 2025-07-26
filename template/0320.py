
def binarysearch(target, ary):
    left, right = 0, len(ary) - 1

    while left <= right:
        mid = (left + right) // 2

        if ary[mid] == target:
            return mid
        elif ary[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def lowerbound(target, ary):
    left, right = 0, len(ary)

    while left < right:
        mid = (left + right) // 2

        if ary[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upperbound(target, ary):
    left, right = 0, len(ary)

    while left < right:
        mid = (left + right) // 2
        
        if ary[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

n = 10
parent = [i for i in range(n + 1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    str = input().rstrip()

    print(str[::-1])

    # ->
    print(str[-1] + str[:-1])
    # <-
    print(str[1:] + str[0])

    from collections import deque
    t = deque(str)
    t.rotate(2)
    print(''.join(t))
    t.rotate(-4)
    print(''.join(t))

    print("reversed(str)")
    a = reversed(str)
    print(list(a))

    print("''.join(reversed(str))")
    print(''.join(reversed(str)))
