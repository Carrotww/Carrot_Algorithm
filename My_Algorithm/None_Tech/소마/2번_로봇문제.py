'''
문제: 자가발전을 하며 연료를 확보할 수 있는 로봇이 처음 주유소에서 출발하여
마지막 주유소까지 도달할 때, 최단시간과 남길 수 있는 최대 연료양을 구하라

조건:
- 각 주유소에서 1초마다 얼만큼의 연료를 채울 수 있는지에 관한 매개변수가 주어진다.

-  각 주유소들이 얼만큼의 간격을 두고 떨어져 있는지에 관한 매개변수가 주어진다.

- 로봇은 첫번째 주유소에 위치해 있으며, 1초에 1만큼의 연료를 소모해 1의 거리를 이동한다.

주어지는게 
1. t초마다 e만큼의 에너지 자가회복
2. gas_list : i번째 주유소에서 초당 얼만큼의 연료를 채울 수 있는지
3. gas_dist : 각 주유소가 얼만큼의 거리가 떨어져있는지
4. fuel: 처음 로봇이 갖고 있는 연료의 양
'''

from typing import List

def solution(t: int, e: int, gas_list: List, gas_dist: List, fuel: int):
    # dp -> time table
    dp = [0] * (sum(gas_dist) + 1)
    cur_time = 0
    dp[0] = fuel

    for i in range(0, len(dp), t):
        dp[i] += e
    
    for i in range(len(gas_list)):
        pass
    
    return

# ()________()__()_________()______________()
def solution(t: int, e: int, gas_list: List, gas_dist: List, fuel: int):
    import heapq
    # 거리, 시간, 연료
    heap = []
    heapq.heappush(heap, (0, 0, -fuel))

    while heap:
        gas_idx, time, fu = heapq.heappop(heap)

        if gas_idx == len(gas_dist) - 1:
            return time

        gas_idx *= -1
        fu *= -1
        
        temp = time // t
        temp = (temp + 1) * t - time
        
        if gas_dist[gas_idx] <= fu:
            pass
        
        heapq.heappush(heap, (-gas_idx, time+1, -(fu + gas_list[gas_idx])))

        while fu > temp and gas_dist[gas_idx] > fu:
            fu += e
            time += t

        if gas_dist[gas_idx] <= fu:
            heapq.heappush(heap, (-(gas_idx+1), time + gas_dist[gas_idx], -(fu - gas_dist[gas_idx])))
        
    return