Here is a Python console application that solves the problem:

```python
def max_profit(prices):
    if len(prices) < 2:
        return 0

    sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0

    for price in prices:
        prev_buy = buy
        buy = max(prev_sell - price, prev_buy)
        prev_sell = sell
        sell = max(prev_buy + price, prev_sell)

    return sell

def main():
    prices = list(map(int, input("Enter the prices separated by space: ").split()))
    print("Maximum profit: ", max_profit(prices))

if __name__ == "__main__":
    main()
```

This console application first asks the user to input the prices separated by space. Then it calculates the maximum profit that can be made from buying and selling stocks with cooldowns using the `max_profit` function. The `max_profit` function uses dynamic programming to keep track of the maximum profit that can be made by buying and selling stocks on each day. The `sell` variable represents the maximum profit that can be made by selling a stock on the current day, while the `buy` variable represents the maximum profit that can be made by buying a stock on the current day. The `prev_sell` and `prev_buy` variables are used to keep track of the maximum profit that can be made by selling or buying a stock on the previous day. The function finally returns the maximum profit that can be made by selling a stock on the last day.