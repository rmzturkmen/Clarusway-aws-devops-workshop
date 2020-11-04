# Calculate Stock Profit

# Bu programin ilk iki satiri ve son iki satiri programin hizini olcmektedir.
from datetime import datetime
now = datetime.now()


lst = [10, 20, 23, 22, 17, 30]


def buy_and_sell(lst):

    max_profit = 0

    for i in range(len(lst)-1):

        for j in range(i+1, len(lst)):

            if lst[j] - lst[i] > max_profit:
                max_profit = lst[j] - lst[i]

    return max_profit


print(buy_and_sell(lst))

later = datetime.now()
print((later - now).total_seconds())
