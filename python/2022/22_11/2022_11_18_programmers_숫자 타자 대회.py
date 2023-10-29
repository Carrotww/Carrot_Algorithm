# https://school.programmers.co.kr/learn/courses/30/lessons/136797

def solution(numbers):
    left, right = 4, 6
    # number_map = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    depth = [
        	[1, 7, 6, 7, 5, 4, 5, 3, 2, 3], # 0
        	[7, 1, 2, 4, 2, 3, 5, 4, 5, 6], # 1
            [6, 2, 1, 2, 3, 2, 3, 5, 4, 5], # 2
    		[7, 4, 2, 1, 5, 3, 2, 6, 5, 4], # 3
    		[5, 2, 3, 5, 1, 2, 4, 2, 3, 5], # 4
    		[4, 3, 2, 3, 2, 1, 2, 3, 2, 3], # 5
    		[5, 5, 3, 2, 4, 2, 1, 5, 3, 2], # 6
    		[3, 4, 5, 6, 2, 3, 5, 1, 2, 4], # 7
    		[2, 5, 4, 5, 3, 2, 3, 2, 1, 2], # 8
    		[3, 6, 5, 4, 5, 3, 2, 4, 2, 1]] # 9
    result = []

    def dfs(number_po, total_val, left, right):
        # number_po 의 위치가 numbers 의 끝까지 갔으면 종료
        if number_po > len(numbers) - 1:
            result.append(total_val)
            return
        change_num = int(numbers[number_po])
        # 움직여야할 다음 번호
        left_val = depth[left][change_num]
        right_val = depth[right][change_num]
        # 왼쪽과 오른쪽의 다음 가중치
        if left_val == 1:
            dfs(number_po + 1, total_val + left_val, change_num, right)
        elif right_val == 1:
            dfs(number_po + 1, total_val + right_val, left, change_num)
        else:
            dfs(number_po + 1, total_val + left_val, change_num, right)
            dfs(number_po + 1, total_val + right_val, left, change_num)
        return
    
    # dfs -> 매개변수 : 현재 numbers의 위치, 지금까지의 가중치, left, right 손가락 위치
    dfs(0, 0, 4, 6)

    return min(result)

    # def dfs(number_po, total_val, left, right):
    #     # number_po 의 위치가 numbers 의 끝까지 갔으면 종료
    #     if number_po > len(numbers) - 1:
    #         result.append(total_val)
    #         return
    #     change_num = int(numbers[number_po])
    #     # 바궈야할 번호
    #     left_val = depth[left][change_num]
    #     right_val = depth[right][change_num]
    #     # 왼쪽과 오른쪽의 다음 가중치
    #     if left_val < right_val:
    #         total_val += left_val
    #         dfs(number_po + 1, total_val, change_num, right)
    #     elif right_val < left_val:
    #         total_val += right_val
    #         dfs(number_po + 1, total_val, left, change_num)
    #     elif left_val == right_val:
    #         total_val += left_val
    #         dfs(number_po + 1, total_val, change_num, right)
    #         dfs(number_po + 1, total_val, left, change_num)
    #     return
    
    # for n in numbers:
    #     num = int(n)
    #     left_val = depth[left][num]
    #     right_val = depth[right][num]
    #     if left_val < right_val:
    #         left = num
    #         cnt += left_val
    #     elif right_val < left_val:
    #         right = num
    #         cnt += right_val
        
    # # dfs -> 매개변수 : 현재 numbers의 위치, 지금까지의 가중치, left, right 손가락 위치
    # dfs(0, 0, 4, 6)

    # return min(result)

print(solution("1756"))
print(solution("5123"))