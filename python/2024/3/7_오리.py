# https://www.acmicpc.net/problem/12933

def find_duck(index):
    global result
    # cur_index -> q
    duck_alpa_index = 1
    for i in range(index+1, len(sound)):
        # print("알파벳 index : ", duck_alpa_index, " duck_dict[sound[i]] : ", duck_dict[sound[i]], " 알파벳 : ", sound[i])
        if duck_dict[sound[i]] == duck_alpa_index and not visited[i]:
            visited[i] = 1
            duck_alpa_index += 1
        if duck_alpa_index == 5:
            duck_alpa_index = 0
    result += 1
    if duck_alpa_index != 0:
        return False
    return True

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    sound = input().strip()
    # q : 0 u : 1 a : 2 c : 3 k : 4
    duck_dict = {}
    quack = 'quack'
    for i in range(len(quack)):
        duck_dict[quack[i]] = i

    visited = [0] * len(sound)
    result = 0
    for i in range(len(sound)):
        if not visited[i] and sound[i] == 'q':
            visited[i] = 1
            if not find_duck(i):
                visited[i] = 0
    if sum(visited) != len(sound):
        print(-1)
    else:
        print(result)

