Here is a Java console application that solves the problem:

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of days:");
        int n = scanner.nextInt();
        int[] prices = new int[n];
        System.out.println("Enter the prices:");
        for (int i = 0; i < n; i++) {
            prices[i] = scanner.nextInt();
        }
        scanner.close();

        if (prices.length <= 1) {
            System.out.println(0);
            return;
        }

        int b0 = -prices[0], b1 = b0;
        int s0 = 0, s1 = 0, s2 = 0;

        for (int i = 1; i < prices.length; i++) {
            b0 = Math.max(b1, s2 - prices[i]);
            s0 = Math.max(s1, b1 + prices[i]);
            b1 = b0; s2 = s1; s1 = s0;
        }
        System.out.println(s0);
    }
}
```

This program reads the number of days and the prices from the console. It then calculates the maximum profit that can be obtained from buying and selling stocks with cooldowns. The result is printed to the console.