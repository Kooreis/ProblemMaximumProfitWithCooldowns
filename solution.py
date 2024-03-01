def max_profit(prices):
    if len(prices) < 2:
        return 0

    sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0