input = 20


def find_prime_list_under_number(number):
    p_list = [x for x in range(2, number + 1)]
    result = []
    for i in p_list:
        if prime(i):
            result.append(i)
    return result

def prime(num):
    temp = [x for x in range(2, num)]
    for i in temp:
        if num % i == 0:
            return False
    return True


result = find_prime_list_under_number(input)
print(result)