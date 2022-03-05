def buy_sell_stock2(prices):
    max_profit, min_buy = 0, float('inf')
    # create an array to hold profits for a single day

    first_profits = [0]*len(prices)
    for i, price in enumerate(prices):
        min_buy = min(min_buy, price)
        max_profit = max(max_profit, price - min_buy)
        first_profits[i] = max_profit

    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_profit = max(
            max_profit, max_price_so_far - price + first_profits[i-1])

    return max_profit


prices = [12, 11, 13, 9, 12, 8, 14, 13, 15]
print(buy_sell_stock2(prices))
