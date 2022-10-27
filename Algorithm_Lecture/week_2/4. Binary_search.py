finding_target = 16
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    cur_min = 0
    cur_max = len(array) - 1
    cur_val = (cur_min + cur_max) // 2
    
    while cur_min <= cur_max:
        if array[cur_val] == target:
            return True
        elif array[cur_val] < target:
            cur_min = cur_val + 1
        else:
            cur_max = cur_val - 1
        cur_val = (cur_min + cur_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)