# https://www.acmicpc.net/problem/2847

def solve():
    import sys
    N = int(sys.stdin.readline())
    num_list = []
    for _ in range(N):
        num_list.append(int(sys.stdin.readline()))
    
    result = 0
    before_num = -1
    for i in range(len(num_list)-1, -1, -1):
        if len(num_list) - 1 == i:
            before_num = num_list[i]
        else:
            cur_num = num_list[i]
            if cur_num >= before_num:
                temp = cur_num
                cur_num = before_num - 1
                result += (temp - cur_num)
            before_num = cur_num
    print(result)

if __name__ == "__main__":
    solve()