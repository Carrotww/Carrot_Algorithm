# https://www.acmicpc.net/problem/2346

# 푸는 중
def solve():
    import sys
    n = int(sys.stdin.readline())
    temp = list(map(int, sys.stdin.readline().split()))
    ball = []
    for idx, val in enumerate(temp):
        ball.append([idx, val])
    
    result = []
    def pop_ball(ball_list, cur_idx, move, n):
        n_idx = cur_idx + move
        if n_idx >= n:
            n_idx -= n
        cur_pop_ball = ball_list.pop(n_idx)

def solve():
    import sys
    n = int(sys.stdin.readline())
    temp = list(map(int, sys.stdin.readline().split()))
    ball = []
    for idx, val in enumerate(temp):
        ball.append([idx, val])

    result = []

    def pop_ball(ball_list, cur_idx, move, n):
        n_idx = (cur_idx + move) % n
        cur_pop_ball = ball_list.pop(n_idx)
        result.append(str(cur_pop_ball[0] + 1))
        return n_idx

    cur_idx = 0
    for _ in range(n):
        move = ball[cur_idx][1]
        cur_idx = pop_ball(ball, cur_idx, move, n)
        n -= 1  # 풍선이 터지므로 전체 풍선 개수 감소

    print(' '.join(result))

if __name__ == "__main__":
    solve()