# https://www.acmicpc.net/problem/1477

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n, m, l = map(int, input().split())
    position = list(map(int, input().split()))
    position.append(0)
    position.append(l)
    position.sort()

    for _ in range(m):
        max_val = 0
        insert_val = 0
        for i in range(1, len(position)):
            if position[i] - position[i-1] > max_val:
                max_val = position[i] - position[i-1]
                insert_val = (position[i] + position[i-1]) // 2
        position.append(insert_val)
        position.sort()

    result = 0
    for i in range(1, len(position)):
        result = max(result, position[i] - position[i-1])
    print(result)

