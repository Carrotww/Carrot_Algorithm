# https://www.acmicpc.net/problem/1963

def check(num):
    if num < 1000:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    import sys
    from collections import deque

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        visited = [0] * 10000
        start, end = input().split()
        start = list(start)
        end = list(end)

        queue = deque([(start, 0)])
        visited[int(''.join(start))] = 1
        result = -1
        while queue:
            cur_num, cnt = queue.popleft()
            if cur_num == end:
                result = cnt
                break
            for i in range(4):
                for j in range(0, 10):
                    n_num = cur_num.copy()
                    n_num[i] = str(j)
                    int_n_num = int(''.join(n_num))
                    if visited[int_n_num] == 0 and check(int_n_num):
                        visited[int_n_num] = 1
                        queue.append((n_num, cnt + 1))
        if result == -1:
            print('Impossible')
        else:
            print(result)
