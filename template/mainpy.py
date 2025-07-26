
if __name__ == "__main__":
    import sys, math
    import heapq

    input = sys.stdin.readline
    print("main call")

class binarySearch:
    def binarySearch(self, target, ary):
        start, end = 0, len(ary) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if ary[mid] == target:
                return mid
            elif ary[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
    
    def lowerbound(self, target, ary):
        start, end = 0, len(ary)

        while start < end:
            mid = (start + end) // 2
            if ary[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start

    def upperbound(self, target, ary):
        start, end = 0, len(ary)
        
        while start < end:
            mid = (start + end) // 2
            if ary[mid] <= target:
                start = mid + 1
            else:
                end = mid
        return start

class unionFind:
    def __init__(self, n):
        self.parent = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x < y:
            self.parent[y] = x
        else:
            self.parent[x] = y
















