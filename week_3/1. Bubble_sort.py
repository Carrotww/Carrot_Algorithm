# https://www.notion.so/3-83a14432311c401598ce3c05e3be25c4

input = [4, 6, 2, 9, 1]

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array

def bubble_sort_my_solve(array):
    cnt = -1
    while cnt != 0:
        cnt = 0
        for i in range(len(array)):
            if i != len(array) - 1 and array[i + 1] < array[i]:
                x = array[i]
                array[i] = array[i + 1]
                array[i + 1] = x
                cnt += 1
        # if cnt == 0:
        #     break
    return array


print(bubble_sort(input))
print(bubble_sort_my_solve(input))