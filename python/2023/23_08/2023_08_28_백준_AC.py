# https://www.acmicpc.net/problem/5430

from collections import deque

def solve():
    result = ''
    fun_list = input().rstrip()

    N = int(input())

    give_list = input().rstrip()
    if give_list == '[]':
        num_list = deque()
    else:
        input_split = give_list.replace('[', '').replace(']', '')
        num_list = deque(map(int, input_split.split(',')))

    reverse = False
    for fun in fun_list:
        if fun == 'R':
            reverse = not reverse
        else:
            if not num_list:
                print('error')
                return
            if reverse:
                num_list.pop()
            else:
                num_list.popleft()
    
    if reverse:
        num_list = reversed(num_list)
    
    print('[' + ','.join(map(str, num_list)) + ']')

if __name__ == "__main__":
    import sys
    
    input = sys.stdin.readline
    # R -> 순서 뒤집기
    # D -> 첫 번째 수 버리기 if empty() -> error
    T = int(input())
    for _ in range(T):
        solve()
