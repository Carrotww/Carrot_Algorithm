input = "abcabcabcabcdededededede"


def string_compression(string):
    result = []
    if len(string) == 1:
        return 1
    
    for word_len in range(1, len(string) // 2 + 1):
        temp = ''
        word_temp = [string[x:x + word_len] for x in range(0, len(string), word_len)]
        cnt = 1
        for i in range(1, len(word_temp)):
            if word_temp[i - 1] == word_temp[i]:
                cnt += 1
            else:
                if cnt == 1:
                    temp += word_temp[i - 1]
                else:
                    temp += (str(cnt) + word_temp[i - 1])
                    cnt = 1
        if cnt > 1:
            temp += str(cnt) + word_temp[-1]
        else:
            temp += word_temp[-1]

        result.append(len(temp))

    return min(result)


print(string_compression(input))  # 14
print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))