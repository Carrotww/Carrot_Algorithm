input = "abcabcabcabcdededededede"


def string_compression(string):
    result = []

    for word_cnt in range(1, len(string) // 2 + 1):
        result_word = ''
        temp_word = [] # 1, 2, 3, 4 기준으로 잘려있는 문자
        for i in range(0, len(string), word_cnt):
            temp_word.append(string[i:i+word_cnt])
        cnt = 1
        for i in range(1, len(temp_word)):
            if temp_word[i - 1] == temp_word[i]:
                cnt += 1
            else:
                if cnt > 1:
                    result_word += str(cnt) + temp_word[i - 1]
                    cnt = 1
                else:
                    result_word += temp_word[i - 1]
                    cnt = 1
        if cnt > 1:
            result_word += str(cnt) + temp_word[-1]
        else:
            result_word += temp_word[-1]
        
        result.append(len(result_word))
    
    return min(result)


print(string_compression(input))  # 14
print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))