top_heights = [6, 9, 5, 7, 4]

# for 문으로 구현하기
def get_receiver_top_orders(heights):
    result = [0]
    n = len(heights)
    for i in range(1, n):
        for j in range(-n + i - 1, -n - 1, -1):
            print(i, j)
            if heights[i] < heights[j]:
                result.append(n + j + 1)
                break
        else:
            result.append(0)
    return result

# Stack 으로 구현하기
def get_receiver_top_orders2(heights):
    result = []
    n = len(heights)
    while heights:
        temp = heights.pop()
        for i in range(len(heights) - 1, 0, -1):
            if heights[i] > temp:
                result.append(i + 1)
                break
        else:
            result.append(0)
    
    return list(reversed(result))


# print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
print(get_receiver_top_orders2(top_heights))