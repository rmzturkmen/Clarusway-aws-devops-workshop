# Calculate Stock Profit

# Bu programin ilk iki satiri ve son iki satiri programin hizini olcmektedir.
from datetime import datetime
now = datetime.now()

#lst = [75, 73, 60, 100, 120, 130]
# lst = [10, 20, 23, 22, 17, 30]
lst = []


def buy_and_sell(lst):

    max_profit, current_max = 0, 0

    for price in reversed(lst):

        current_max = max(current_max, price)

        potential_profit = current_max - price

        max_profit = max(potential_profit, max_profit)

    return max_profit


print(buy_and_sell(lst))

later = datetime.now()
print((later - now).total_seconds())
