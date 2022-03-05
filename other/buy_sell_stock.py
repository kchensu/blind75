def buy_sell_stock(prices):
    min_buy = float('inf')
    max_sell = 0

    for price in prices:
        if price < min_buy:
            min_buy = price
        elif price - min_buy > max_sell:
            max_sell = price - min_buy
    return max_sell


a = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_sell_stock(a))
