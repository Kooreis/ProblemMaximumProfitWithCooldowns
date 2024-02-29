Here is a C# console application that solves the problem:

```CSharp
using System;

class Program
{
    static void Main(string[] args)
    {
        int[] prices = { 1, 2, 3, 0, 2 };
        Console.WriteLine(MaxProfit(prices));
    }

    static int MaxProfit(int[] prices)
    {
        if (prices.Length <= 1) return 0;
        int[] s0 = new int[prices.Length];
        int[] s1 = new int[prices.Length];
        int[] s2 = new int[prices.Length];
        s0[0] = 0;
        s1[0] = -prices[0];
        s2[0] = int.MinValue;
        for (int i = 1; i < prices.Length; i++)
        {
            s0[i] = Math.Max(s0[i - 1], s2[i - 1]);
            s1[i] = Math.Max(s1[i - 1], s0[i - 1] - prices[i]);
            s2[i] = s1[i - 1] + prices[i];
        }
        return Math.Max(s0[prices.Length - 1], s2[prices.Length - 1]);
    }
}
```

This program uses dynamic programming to solve the problem. It maintains three states, s0, s1, and s2, representing the maximum profit up to the current day in the cooldown, buy, and sell states, respectively. It then iterates over the prices, updating the states based on the maximum profit that can be achieved by transitioning from the previous state. The maximum profit is the maximum of the cooldown and sell states on the last day.