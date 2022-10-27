# https://www.notion.so/4-c777c38a75654648bd8c35522c43fc75
seat_count = 9
vip_seat_array = [4, 7]


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    def fibo(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        temp = [0, 1, 2]
        for i in range(3, n + 1):
            temp.append(temp[i - 1] + temp[i - 2])
        
        return temp[-1]
    
    result = 1
    for cnt in range(len(fixed_seat_array)):
        if cnt == 0:
            if fixed_seat_array[0] == 1:
                continue
            result *= fibo(fixed_seat_array[0] - 1)
        else:
            result *= fibo(fixed_seat_array[cnt] - fixed_seat_array[cnt - 1] - 1)
    if fixed_seat_array[-1] < total_count:
        result *= fibo(total_count - fixed_seat_array[-1])
    
    return result

print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))