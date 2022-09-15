shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    result = 0
    coupons.sort()
    prices.sort()
    
    while coupons:
        result += (100 - coupons.pop()) / 100 * (prices.pop())
    for i in prices:
        result += i
        
    return int(result)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000