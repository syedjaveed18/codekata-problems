n = int(input())
price = list(map(int,input().split()))

min_price = min(price)
print("Dealer"+str(price.index(min_price)))
