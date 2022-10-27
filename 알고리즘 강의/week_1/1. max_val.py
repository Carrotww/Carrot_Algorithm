input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for arr in array:
        for comp in array:
            if arr < comp:
                break
        else:
            return arr

    return result


result = find_max_num(input)
print(result)