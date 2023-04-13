# https://www.acmicpc.net/problem/14888

# 내 풀이
if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())

    num_list = list(map(int, sys.stdin.readline().split()))
    oper_list = list(map(int, sys.stdin.readline().split()))
    oper_dict = {'+': oper_list[0], '-': oper_list[1], '*': oper_list[2], '//': oper_list[3]}
    num_list.reverse()
    result = []

    def solve(total, cur_num_list, cur_oper_list):
        if not cur_num_list:
            result.append(total)
            return
        
        cur_num = cur_num_list.pop()
        
        for i in range(4):
            temp_num = total
            if cur_oper_list[i] == 0:
                continue
            temp_cur_oper_list = cur_oper_list[:]
            temp_cur_oper_list[i] -= 1

            if i == 0:
                temp_num += cur_num
            elif i == 1:
                temp_num -= cur_num
            elif i == 2:
                temp_num *= cur_num
            elif i == 3:
                if temp_num < 0 and cur_num > 0:
                    temp_num *= -1
                    temp_num = temp_num // cur_num
                    temp_num *= -1
                else:
                    temp_num = temp_num // cur_num
            
            solve(temp_num, cur_num_list[:], temp_cur_oper_list)
    
    num = num_list.pop()
    solve(num, num_list[:], oper_list[:])

    print(max(result))
    print(min(result))