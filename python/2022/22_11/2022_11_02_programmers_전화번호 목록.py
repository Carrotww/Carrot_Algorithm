# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort()
    
    for a, b in zip(phone_book, phone_book[1:]):
        if a == b[0:len(a)]:
            return False
    return True

# hash로 품
def solution2(phone_book):
    phone_book.sort(reverse=True)
    temp_dict = {x for x in phone_book}

    for num in phone_book:
        temp = ''
        for n in num:
            temp += n
            if temp in temp_dict and temp != num:
                return False
    return True