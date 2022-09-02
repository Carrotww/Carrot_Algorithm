input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    result = 0
    for i in range(len(array)):
        if array[i] < 2 or result < 2:
            result += array[i]
        else:
            result *= array[i]

    return result


result = find_max_plus_or_multiply(input)
print(result)