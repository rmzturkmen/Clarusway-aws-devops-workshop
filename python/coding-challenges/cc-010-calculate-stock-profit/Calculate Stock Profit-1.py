# Calculate Stock Profit

# Bu programin ilk iki satiri ve son iki satiri programin hizini olcmektedir.
from datetime import datetime
now = datetime.now()

lst = [1, 6, 19, 59, 30, 60]


def buy_and_sell(lst):

    max_profit = 0
    min_price = lst[0]

    for price in lst:

        min_price = min(min_price, price)

        compare_profit = price - min_price

        max_profit = max(max_profit, compare_profit)

    return max_profit


print(buy_and_sell(lst))

later = datetime.now()
print((later - now).total_seconds())
