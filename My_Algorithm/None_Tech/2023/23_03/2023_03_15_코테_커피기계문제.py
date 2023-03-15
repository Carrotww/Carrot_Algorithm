def solution(N, coffee_times):
    import heapq
    result = []
    heap = []
    for i in range(N):
        heapq.heappush(heap, (coffee_times[i], i))

    for i in range(N, len(coffee_times)):
        time, idx = heapq.heappop(heap)
        result.append(idx+1)
        heapq.heappush(heap, (coffee_times[i]+time, i))
    
    while heap:
        time, idx = heapq.heappop(heap)
        result.append(idx+1)
        
    return result

print(solution(3, [4, 2, 2, 5, 3]))
print(solution(1, [100, 1, 50, 1, 1]))