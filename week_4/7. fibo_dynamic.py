input = 50

memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, dp):
    if n in dp:
        return dp[n]

    temp =  fibo_dynamic_programming(n - 1, dp) + fibo_dynamic_programming(n - 2, dp)
    dp[n] = temp
    return temp


print(fibo_dynamic_programming(input, memo))