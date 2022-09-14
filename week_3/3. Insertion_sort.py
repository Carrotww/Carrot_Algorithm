input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
            else:
                break
        
    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9]


array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    # 이 곳을 채워보세요!
    return array