# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    result = ''
    # 1. 앞자리 무조건 큰게 앞으로 온다
    # 2. 만약 앞자리 숫자가 같으면 뒤 숫자를 비교해서 앞자리보다 크면 먼저, 작으면 뒤로
    # 3. ex) 7, 76, 78 이라면 78 -> 7 -> 76

    # number 원소가 1000 이하이므로 다 4자리로 만들어버리고 비교하면 됨
    # 라고 생각했었는데 121, 12 가 온다면 내 코드는 뭐가 나올줄 모름
    # 답은 12121 이 나와야함

    for i in range(len(numbers)):
        cur_num = numbers[i]
        # str_num = str(cur_num)
        # while len(str_num) < 5:
        #     str_num += str_num[0]
        # numbers[i] = [str(cur_num), int(str_num)]
        numbers[i] = [str(cur_num), str(cur_num) * 4]


    numbers.sort(key=lambda x:x[1], reverse=True)
    for a, b in numbers:
        result += a
    if int(result):
        return result
    return '0'

