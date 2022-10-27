import copy

numbers = [1, 1, 1, 1, 1]
numbers2 = [4, 1, 2, 1]
target_number = 3
target_number2 = 4

def plus_or_minus(numbers, target):
    result = [0]
    for num in numbers:
        temp = []
        for re in result:
            temp.append(re + num)
            temp.append(re - num)
        result = temp
    return result.count(target)

def pm2(numbers, target):
    # Recursive_version
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return pm2(numbers[:-1], target-numbers[-1]) + pm2(numbers[:-1], target+numbers[-1])

def pm3(numbers, target):
    # Recursive_version
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        temp_list = copy.deepcopy(numbers)
        temp = temp_list.pop()
        return pm3(temp_list, target-temp) + pm3(temp_list, target+temp)

print(plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
print(pm2(numbers, target_number))
print(pm3(numbers, target_number))

print(pm2(numbers2, target_number2))
print(pm3(numbers2, target_number2))