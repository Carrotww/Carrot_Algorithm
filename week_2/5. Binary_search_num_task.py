finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    numbers.sort()
    ary_min = 0
    ary_max = len(numbers) - 1
    ary_val = (ary_min + ary_max) // 2

    while ary_min <= ary_max:
        if numbers[ary_val] == target:
            return True
        elif target < numbers[ary_val]:
            ary_max = ary_val - 1
        else:
            ary_min = ary_val + 1
        ary_val = (ary_max + ary_min) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)