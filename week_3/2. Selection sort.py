input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[min_index] > array[i + j]:
                min_index = i + j
        array[min_index], array[i] = array[i], array[min_index]

    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9]