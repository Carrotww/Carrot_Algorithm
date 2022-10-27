from collections import defaultdict
from pprint import pprint

genres1 = ["classic", "pop", "classic", "classic", "pop"]
plays1 = [500, 600, 150, 800, 2500]

genres2 = ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"]
plays2 = [2000, 500, 600, 150, 800, 2500, 2000]

def get_melon_best_album(genre_array, play_array):
    temp = {}
    count_dict = defaultdict(int)
    for i in range(len(genre_array)):
        temp[i] = [genre_array[i], play_array[i]]
        count_dict[genre_array[i]] += play_array[i]
    result = []

    count_dict = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)
    temp = sorted(temp.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True)
    
    for i in range(len(count_dict)):
        cnt = 0
        for j in range(len(genre_array)):
            if temp[j][1][0] == count_dict[i][0] and cnt < 2:
                result.append(temp[j][0])
                cnt += 1
        
    return result


print(get_melon_best_album(genres1, plays1))  # [4, 1, 3, 0]
print(get_melon_best_album(genres2, plays2))  # [0, 6, 5, 2, 4, 1]