def bubble_sort(ary):
    for i in range(len(ary)-1, 0, -1):
        for j in range(i):
            if ary[j] > ary[j+1]:
                ary[j], ary[j+1] = ary[j+1], ary[j]
    
    return ary

print(bubble_sort([3, 5, 1, 6, 2, 10]))