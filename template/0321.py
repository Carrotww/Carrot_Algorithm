
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
parent = [x for x in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y
