# https://www.acmicpc.net/problem/22862

def solve():
    import sys
    N, K = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = []
    # b 짝수 -> 0 홀수 -> 1
    for val in a:
        if val % 2 == 0:
            b.append(0)
        else:
            b.append(1)
    
    result = 0
    cnt = 0
    end = 0
    temp = 0
    for idx in range(len(b)):
        while cnt <= K and end < N:
            # 홀수이면 cnt + 1
            if b[end] == 1:
                cnt += 1
            else:
                temp += 1
            end += 1

            if idx == 0 and end == N:
                result = temp
                break
        if cnt == K+1:
            result = max(result, temp)
        if b[idx] == 1:
            cnt -= 1
        else:
            temp -= 1
    
    print(result)

if __name__ == "__main__":
    solve()