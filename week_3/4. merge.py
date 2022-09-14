array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    result = []
    ary_index_1 = 0
    ary_index_2 = 0
    
    while ary_index_1 < len(array1) and ary_index_2 < len(array2):
        if array1[ary_index_1] < array2[ary_index_2]:
            result.append(array1[ary_index_1])
            ary_index_1 += 1
        else:
            result.append(array2[ary_index_2])
            ary_index_2 += 1
    
    if ary_index_1 < len(array1):
        for i in range(ary_index_1, len(array1)):
            result.append(array1[i])
    else:
        for i in range(ary_index_2, len(array2)):
            result.append(array2[i])
            
    return result


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!