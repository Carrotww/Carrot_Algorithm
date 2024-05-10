def checkbingo(player, graph):
    # 媛濡?泥댄겕
    for i in range(3):
        cnt = 0
        for j in range(3):
            if graph[i][j] == player:
                cnt += 1
        if cnt == 3:
            return True

    # ?몃줈 泥댄겕
    for i in range(3):
        cnt = 0
        for j in range(3):
            if graph[j][i] == player:
                cnt += 1
        if cnt == 3:
            return True

    # ?媛곸꽑 泥댄겕
    start_r, start_c = 0, 0
    cnt = 0
    for i in range(3):
        if graph[start_r + i][start_c + i] == player:
            cnt += 1
    if cnt == 3:
        return True

    start_r, start_c = 0, 2
    cnt = 0
    for i in range(3):
        if graph[start_r + i][start_c - i] == player:
            cnt += 1
    if cnt == 3:
        return True

    return False


def solve(t):
    graph = []
    start = 0
    for _ in range(3):
        graph.append(t[start:start + 3])
        start += 3

    cur_o, cur_x, cur_b = 0, 0, 0
    for i in range(3):
        for j in range(3):
            if graph[i][j] == 'O':
                cur_o += 1
            elif graph[i][j] == 'X':
                cur_x += 1
            else:
                cur_b += 1

    if cur_o > cur_x or not cur_o + 1 >= cur_x:
        return False

    if cur_o <= cur_x:
        # 'O'媛 鍮숆퀬瑜??ъ꽦?덈뒗吏 ?뺤씤?섎뒗 濡쒖쭅
        if checkbingo('O', graph):
            return False

    if cur_o == cur_x and cur_b:
        if checkbingo('X', graph):
            return False

    # 鍮숆퀬 ?곹깭瑜??뺤씤?섎뒗 濡쒖쭅
    if not checkbingo('O', graph) and not checkbingo('X', graph) and cur_b:
        return False

    return True


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    graph = []
    result = []

    while True:
        t = list(input().strip())
        if t[0] == 'e':
            break
        if solve(t):
            result.append('valid')
        else:
            result.append('invalid')

    for r in result:
        print(r)

