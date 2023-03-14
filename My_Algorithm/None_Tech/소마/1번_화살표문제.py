# 입력값 str : '--->', '<--->----><---->'
'''
입력으로 ‘<’, ‘>’, ‘-’ 로 이루어진 문자열이 주어진다.
이 문자열을 우리는 
1. 왼쪽을 의미하는 화살표: <--..--
2. 오른쪽을 의미하는 화살표: --..-->
3. 양쪽을 의미하는 화살표: <--..-->
들로 구분할 수 있다.

입력으로 왼쪽 오른쪽 화살표가 연이어서 주어지는 상황은 없다.
이 때 문자열이 주어지면 해당 문자열이 얼만큼의 길이의 어떤 화살표들로 이루어져 있는지 배열에 담아 출력하라.

-1은 왼쪽 화살표
0 은 양쪽 화살표
1 은 오른쪽 화살표를 뜻하며

예시로 <---<-->-><--
라는 입력이 주어졌을 경우
길이 3짜리 왼쪽, 길이 2짜리 양쪽, 길이 1짜리 오른쪽, 길이 2짜리 왼쪽으로 구성되어있는 문자열이기에
답은 [[-1, 3], [0, 2], [1, 1], [-1, 2]] 가 정답이다.
'''

def solution(arrow):
    stack = list(arrow)
    result = []

    while stack:
        cur_char = stack.pop()
        # 왼쪽 화살표인 경우
        if cur_char == '-':
            cnt = 1
            while stack[-1] != '<':
                stack.pop()
                cnt += 1
            stack.pop()
            result.append([-1, cnt])
        else:
            pass

    return result[::-1]

print(solution('---->')) # [[1, 4]]
print(solution('<---->')) # [[0, 4]]
print(solution('<-----<-----<-->-><--')) #[[-1,5], [-1,5], [0,2], [1, 1], [-1,2]]
print(solution('<---><--><->-->')) # [[0, 3], [0, 2], [0, 1], [1, 2]]




def sol(arrow_string):
    result = []
    idx = 0
    limit = len(arrow_string)
    curr_mark = None
    count = 0
    while idx < limit:
        if arrow_string[idx] == '-':
            count += 1

        elif arrow_string[idx] == '<':
            if curr_mark == '<':
                result.append([-1, count])
            curr_mark = '<'
            count = 0

        elif arrow_string[idx] == '>':
            if curr_mark == '<':
                result.append([0, count])
                curr_mark = None
                count = 0
            else:
                result.append([1, count])
                curr_mark = None
                count = 0
        else:
            print('wrong input. string is only consist of ">", "<", "-"')
        idx += 1

    if count > 0:
        result.append([-1, count])
    return result


print(sol('---->')) # [[1, 4]]
print(sol('<---->')) # [[0, 4]]
print(sol('<-----<-----<-->-><--')) #[[-1,5], [-1,5], [0,2], [1, 1], [-1,2]]
print(sol('<---><--><->-->')) # [[0, 3], [0, 2], [0, 1], [1, 2]]


def sol2(arrow_string):
    arrow_dict = {'<': -1, '>': 1, '-': 0}
    result = []
    idx = 0
    limit = len(arrow_string)
    curr_mark = None
    count = 0
    while idx < limit:
        char = arrow_string[idx]
        if char == '-':
            count += 1
        elif char in arrow_dict:
            arrow_val = arrow_dict[char]
            if curr_mark == '<':
                result.append([0, count]) if arrow_val == 1 else result.append([-1, count])
                curr_mark = None
                count = 0
            else:
                result.append([arrow_val, count])
                curr_mark = char
                count = 0
        idx += 1
    if count > 0:
        result.append([-1, count])
    return result

print(sol2('---->')) # [[1, 4]]
print(sol2('<---->')) # [[0, 4]]
print(sol2('<-----<-----<-->-><--')) #[[-1,5], [-1,5], [0,2], [1, 1], [-1,2]]
print(sol2('<---><--><->-->')) # [[0, 3], [0, 2], [0, 1], [1, 2]]