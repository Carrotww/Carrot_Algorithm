def find_alphabet_occurrence_array(string):
    array = [0] * 26
    max_alpa = 0
    max_cnt = 0
    for st in string:
        if not st.isalpha():
            continue
        temp = ord(st) - ord('a')
        array[temp] += 1
    for i in range(len(array)):
        alpa_cnt = array[i]
        if alpa_cnt > max_cnt:
            max_cnt = alpa_cnt
            max_alpa = i
    result = chr(max_alpa + ord('a'))

    return result, max_cnt


print(find_alphabet_occurrence_array("hello my name is spabbbbbmmmmmmmmmrta"))