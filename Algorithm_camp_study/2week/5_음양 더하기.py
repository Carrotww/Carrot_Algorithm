# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    return sum(num if si else -num for num, si in zip(absolutes, signs))

# def solution(absolutes, signs):
#     join_list = zip(absolutes, signs)
#     result = 0
#     for ab, si in join_list:
#         if si:
#             result += ab
#             continue
#         result -= ab
#     return result