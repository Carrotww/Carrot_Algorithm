def bubble_sort(ary):
    for i in range(len(ary)-1, 0, -1):
        for j in range(i):
            if ary[j] > ary[j+1]:
                ary[j], ary[j+1] = ary[j+1], ary[j]
    
    return ary

def bubble_sort_advance(ary):
    for i in range(len(ary)-1, 0, -1):
        swap = False
        for j in range(i):
            if ary[j] > ary[j+1]:
                ary[j], ary[j+1] = ary[j+1], ary[j]
                swap = True
        if not swap:
            break

print(bubble_sort([3, 5, 1, 6, 2, 10]))