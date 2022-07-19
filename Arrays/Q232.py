n = int(input())
stock_prices = list(map(int,input().split()))

max_profit = 0
for day,stock1 in enumerate(stock_prices):
    for stock2 in stock_prices[day+1:]:
        profit = stock2 - stock1
        if profit >= max_profit:
            max_profit = profit

print(max_profit)
