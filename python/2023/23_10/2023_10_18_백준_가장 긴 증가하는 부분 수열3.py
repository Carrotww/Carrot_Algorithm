# https://www.acmicpc.net/problem/12738

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    b = [a[0]]
    for i in range(1, n):
        if b[-1] < a[i]:
            b.append(a[i])
        else:
            target = a[i]
            left, right = 0, len(b)
            while left < right:
                mid = (left + right) // 2
                if b[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            b[right] = target
    print(len(b))
