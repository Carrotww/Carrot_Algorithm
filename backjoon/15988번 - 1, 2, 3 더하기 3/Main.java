/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 15988                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/15988                          #+#        #+#      #+#    */
/*   Solved: 2025/11/03 15:18:54 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {
    static int result;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());
        final int maxSize = 1_000_001;
        final int mod = 1_000_000_009;

        int[] dp = new int[maxSize];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        for (int i = 4; i < maxSize; i++) {
            long sum = (long) dp[i - 1] + dp[i - 2] + dp[i - 3];
            dp[i] = (int) (sum % mod);
        }

        StringBuilder sb = new StringBuilder();

        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());

            sb.append(dp[n]);
            sb.append("\n");
        }
        System.out.println(sb);
    }
}