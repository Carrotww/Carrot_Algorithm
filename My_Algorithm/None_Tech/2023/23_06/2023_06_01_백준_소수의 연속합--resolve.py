# https://www.acmicpc.net/problem/1644

def prime_list(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    return [x for x in range(n+1) if is_prime[x]]

def solve():
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

if __name__ == "__main__":
    solve()