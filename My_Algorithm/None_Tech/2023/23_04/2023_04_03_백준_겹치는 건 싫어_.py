# https://www.acmicpc.net/problem/20922

from collections import defaultdict

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    data = list(map(int, input().split()))

    max_val = 0

    left, right = 0, 0
    
    check_dict = defaultdict(int)

    # while right < n and left <= right:
    #     # check_dict[data[right]] += 1
    #     if check_dict[data[right]]+1 > k: 
    #         check_dict[data[left]] -= 1
    #         left += 1
    #     else:
    #         check_dict[data[right]] += 1
    #         max_val = max(max_val, right - left + 1)
    #         right += 1

    while right < n and left <= right:
        check_dict[data[right]] += 1
        if check_dict[data[right]] > k: 
            check_dict[data[left]] -= 1
            check_dict[data[right]] -= 1
            left += 1
        else:
            max_val = max(max_val, right - left + 1)
            right += 1
    
    print(max_val)