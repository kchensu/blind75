def buyAndSellStocks(a):
    minBuy = float('inf')
    maxProfit = 0

    for price in a:
        if price < minBuy:
            minBuy = price
        elif price - minBuy > maxProfit:
            maxProfit = price - minBuy
    return maxProfit


prices = [7, 1, 5, 3, 6, 4]
print(buyAndSellStocks(prices))
