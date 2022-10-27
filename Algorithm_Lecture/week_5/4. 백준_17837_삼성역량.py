from pprint import pprint

k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def change_d(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    current_stacked_horse_map = [[[] for _ in range(len(game_map))] for _ in range(len(game_map))]
    for i in range(len(horse_location_and_directions)):
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i)
    cnt = 1
    
    while cnt <= 1000:
        for horse_index in range(horse_count):
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d]
            new_c = c + dc[d]
            if not 0 <= new_r < len(game_map) or not 0 <= new_c < len(game_map) or game_map[new_r][new_c] == 2:
                new_d = change_d(d)
                horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]
                
                if not 0 <= new_r < len(game_map) or not 0 <= new_c < len(game_map) or game_map[new_r][new_c] == 2:
                    continue
            moving_horse_index = []
            for i in range(len(current_stacked_horse_map[r][c])):
                current_index = current_stacked_horse_map[r][c][i]
                if horse_index == current_index:
                    moving_horse_index = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                    break
            if game_map[new_r][new_c] == 1:
                moving_horse_index = reversed(moving_horse_index)
            
            for moving in moving_horse_index:
                current_stacked_horse_map[new_r][new_c].append(moving)
                horse_location_and_directions[moving][0], horse_location_and_directions[moving][1] = new_r, new_c
            
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return cnt
        cnt += 1
    return -1
    pprint(current_stacked_horse_map)
    return


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다