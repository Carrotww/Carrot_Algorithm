# https://www.acmicpc.net/problem/1644

def prime_list(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    return [x for x in range(n+1) if is_prime[x]]


def solve1():
    import sys
    num = int(sys.stdin.readline())
    primes = prime_list(num)
    sum_list = [0] * (len(primes) + 1)
    cnt = 0

    for i in range(1, len(primes) + 1):
        sum_list[i] = sum_list[i-1] + primes[i-1]

    for i in range(len(primes)):
        for j in range(i+1, len(primes)+1):
            if sum_list[j] - sum_list[i] == num:
                cnt += 1
            elif sum_list[j] - sum_list[i] > num:
                break

    print(cnt)


def solve():
    import sys
    num = int(sys.stdin.readline())
    if num == 1:
        print(0)
        return
    primes = prime_list(num)

    total = primes[0]
    start, end = 0, 0
    result = 0
    while end <= len(primes):
        if total == num:
            result += 1
            end += 1
            if end < len(primes):
                total += primes[end]
            else:
                break
        elif total < num:
            end += 1
            if end < len(primes):
                total += primes[end]
            else:
                break
        else:
            total -= primes[start]
            start += 1

    print(result)

if __name__ == "__main__":
    solve()
