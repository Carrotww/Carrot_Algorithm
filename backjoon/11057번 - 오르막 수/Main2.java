/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 11057                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/11057                          #+#        #+#      #+#    */
/*   Solved: 2025/07/31 15:50:35 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main2 {
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        int[][] dp = new int[N+1][10];

        Arrays.fill(dp[1], 1);

        for (int digit = 2; digit < N+1; digit++) {
            dp[digit][0] = 1;
            for (int lastNum = 1; lastNum < 10; lastNum++) {
                dp[digit][lastNum] = dp[digit-1][lastNum] + dp[digit][lastNum-1];
                dp[digit][lastNum] %= 10007;
            }
        }

        int result = 0;

        for (int i = 0; i < 10; i++) {
            result += dp[N][i];
            result %= 10007;
        }

        System.out.println(result);
    }
}