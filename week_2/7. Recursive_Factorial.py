def factorial(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return n * factorial(n - 1)

for i in range(1, 7):
    print(i, factorial(i))