# https://www.acmicpc.net/problem/14499

def move_dice(dice, direct):
    # 1 -> right, 2 -> left, 3 -> up, 4 -> down
    # dice = [1, 2, 3, 4, 5, 6]
    new_dice = []
    if direct == 1:
        new_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif direct == 2:
        new_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif direct == 3:
        new_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif direct == 4:
        new_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    return new_dice


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    row, col, r, c, command_cnt = map(int, input().split())
    command = []
    graph = []
    for _ in range(row):
        temp = list(map(int, input().split()))
        graph.append(temp)

    dice = [0, 0, 0, 0, 0, 0]
    move_direct = list(map(int, input().split()))
    move = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
    result = []

    for direct in move_direct:
        n_r, n_c = r+move[direct][0], c+move[direct][1]
        if (n_r < 0 or n_r >= row) or (n_c < 0 or n_c >= col):
            continue
        r, c = n_r, n_c

        dice = move_dice(dice, direct)
        dice_bottom = dice[5]
        dice_top = dice[0]

        if graph[r][c] == 0:
            graph[r][c] = dice_bottom
        else:
            dice[-1] = graph[r][c]
            graph[r][c] = 0

        result.append(dice_top)

    for r in result:
        print(r)
