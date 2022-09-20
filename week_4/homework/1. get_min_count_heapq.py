# https://www.notion.so/4-c777c38a75654648bd8c35522c43fc7
import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    cnt, date_index = 0, 0
    heap = []

    while stock <= k:
        while date_index < len(dates) and dates[date_index] <= stock:
            heapq.heappush(heap, -supplies[date_index])
            date_index += 1
        cnt += 1
        stock += -heapq.heappop(heap)
        
    return cnt

print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))