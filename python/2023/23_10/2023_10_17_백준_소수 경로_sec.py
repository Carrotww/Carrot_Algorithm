# https://www.acmicpc.net/problem/1963

# 두 번째 풀이

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
        start, end = input().split()
        start, end = list(start), list(end)

        queue = deque([(start, 0)])
        result = -1
        visited = [0] * 10000
        visited[int(''.join(start))] = 1
        while queue:
            cur_val, cnt = queue.popleft()
            if cur_val == end:
                result = cnt
                break
            for i in range(4):
                for num in range(10):
                    temp_num = cur_val[:]
                    temp_num[i] = str(num)
                    int_temp_num = int(''.join(temp_num))
                    if visited[int_temp_num] == 0 and check(int_temp_num):
                        visited[int_temp_num] = 1
                        queue.append((temp_num, cnt + 1))
        
        if result == -1:
            print("Impossible")
        else:
            print(result)