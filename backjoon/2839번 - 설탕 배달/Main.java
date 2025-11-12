/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2839                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2839                           #+#        #+#      #+#    */
/*   Solved: 2025/11/11 21:45:23 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] dp = new int[5001];
        dp[3] = 1;
        dp[5] = 1;

        for (int i = 6; i <= N; i++) {
            if (dp[i - 3] != 0) {
                dp[i] = dp[i - 3] + 1;
            }

            if (dp[i - 5] != 0) {
                if (dp[i] == 0) {
                    dp[i] = dp[i - 5] + 1;
                } else {
                    dp[i] = Math.min(dp[i - 5] + 1, dp[i]);

                }
            }
        }

        if (dp[N] == 0) {
            System.out.println(-1);
        } else {
            System.out.println(dp[N]);
        }
    }
}