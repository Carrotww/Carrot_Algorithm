# https://school.programmers.co.kr/learn/courses/30/lessons/77884

# 마지막 풀이
def fun1(num):
    result = [x for x in range(1, num // 2 + 1) if num % x == 0]
    result.append(num)
    return num if len(result) % 2 == 0 else -num

def solution(left, right):
    return sum([fun1(x) for x in range(left, right + 1)])

# # 2 번 풀이
# def fun1(num):
#     result = [x for x in range(1, num // 2 + 1) if num % x == 0]
#     result.append(num)
#     return num if len(result) % 2 == 0 else -num

# def solution(left, right):
#     result = 0
#     for i in range(left, right + 1):
#         result += fun1(i)
#     return result



# # 1 번 풀이
# def fun1(num):
#     result = [x for x in range(1, num // 2 + 1) if num % x == 0]
#     result.append(num)
#     return True if len(result) % 2 == 0 else False

# def solution(left, right):
#     result = 0
#     for i in range(left, right + 1):
#         if fun1(i):
#             result += i
#         else:
#             result -= i
#     return result
