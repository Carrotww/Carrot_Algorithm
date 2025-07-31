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

public class Main {
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        int[][] dp = new int[N][10];

        for (int i = 0; i < 10; i++) {
            dp[0][i] = 1;
        }

        for (int i = 0; i < N; i++) {
            dp[i][9] = 1;
        }

        for (int i = 1; i < N; i++) {
            for (int j = 8; j >= 0; j--) {
                dp[i][j] = dp[i-1][j] + dp[i][j+1];
                dp[i][j] %= 10007;
            }
        }

        System.out.println(Arrays.stream(dp[N-1]).sum() % 10007);
    }
}