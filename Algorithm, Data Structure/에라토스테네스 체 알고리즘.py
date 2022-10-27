import math

def find_prime(num: int) -> list:
    num_list = [True for i in range(num + 1)]
    prime_list = []

    for i in range(2, int(math.sqrt(num)) + 1):
        if num_list[i] == True:
            j = 2
            while i * j <= num:
                num_list[i * j] = False
                j += 1
    for i in range(2, num + 1):
        if num_list[i] == True:
            prime_list.append(i)

    return prime_list

print(find_prime(23))
print(find_prime(101))
print(find_prime(1001))