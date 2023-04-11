# https://www.acmicpc.net/problem/14888

if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())

    num_list = list(map(int, sys.stdin.readline().split()))
    oper_list = list(map(int, sys.stdin.readline().split()))
    oper_dict = {'+': oper_list[0], '-': oper_list[1], '*': oper_list[2], '%': oper_list[3]}