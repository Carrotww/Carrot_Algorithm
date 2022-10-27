T = int(input())

cnt = 0
for i in range(T):
    temp = input()
    compare_list = []
    if len(temp) == 1:
        cnt += 1
        continue
    for i in temp:
        if compare_list and i == compare_list[-1]:
            continue
        else:
            compare_list.append(i)
    if len(compare_list) == len(set(compare_list)):
        cnt += 1

print(cnt)