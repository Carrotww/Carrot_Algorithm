# https://www.acmicpc.net/problem/1038

def solve():
    import sys
    N = int(sys.stdin.readline())

    if N == 0:
        print(0)
        return
    
    def check(num):
        num = str(num)
        if len(num) == 1:
            return True
        else:
            temp = num[0]
            for i in range(1, len(num)):
                if int(num[i]) >= int(temp):
                    return False
                temp = num[i]
        
        return True

    cnt = 0
    result = -1
    for i in range(1, 1000001):
        # print(i)
        temp = check(i)
        # print(temp)
        if temp:
            cnt += 1
        if cnt == N:
            result = i
            break
    
    print(result)

# bfs

def solve():
    from collections import deque
    import sys
    N = int(sys.stdin.readline())
    
    if N < 10:
        print(N)
        return

    cnt = 9
    queue = deque(range(1, 10))

    while queue:
        num = queue.popleft()

        last_digit = num % 10

        for i in range(last_digit):
            next_num = num * 10 + i
            queue.append(next_num)
            cnt += 1

            if cnt == N:
                print(next_num)
                return

    print(-1)

if __name__ == "__main__":
    solve()