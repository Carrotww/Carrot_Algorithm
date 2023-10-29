# https://www.acmicpc.net/problem/13335

if __name__ == "__main__":
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, w, L = map(int, input().split())
    truck = list(map(int, input().split()))
    truck = deque(truck)
    queue = deque([0 for _ in range(w)])

    total = truck[0]
    queue[-1] = truck.popleft()
    time = 1
    while truck:
        cur_truck = queue.popleft()
        # 첫번째 값을 뺀 후 다음 값이 들어올 수 있는 경우
        # 없는 경우
        time += 1
        total -= cur_truck
        if total + truck[0] <= L:
            n_truck = truck.popleft()
            queue.append(n_truck)
            total += n_truck
        else:
            queue.append(0)
        
    for i in range(w-1, -1, -1):
        if queue[i] != 0:
            time += (i + 1)
            break

    print(time)
