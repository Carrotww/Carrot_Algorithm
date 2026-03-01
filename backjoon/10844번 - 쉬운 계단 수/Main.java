/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 10844                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/10844                          #+#        #+#      #+#    */
/*   Solved: 2026/02/26 21:23:31 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        long div = 1_000_000_000;
        long result = 0;

        long[][] dp = new long[N + 1][10];

        // 상태를 나타낼 수 있는가?
        // 길이가 N 이면서 마지막 자리가 M 인 수까지 오려면?
        // dp[N][M] = dp[N-1][M-1] + dp[N-1][M+1]
        // N -> 주어짐, M -> 0~9
        // 초기화 : N -> 1 일 때 M 들을 초기화 한 후 botton up 방식으로 계산
        // div 신경 쓰기

        for (int i = 1; i < 10; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i < N + 1; i++) {
            for (int j = 0; j < 10; j++) {
                long sum = 0;
                if (j == 0) {
                    sum = dp[i-1][j+1];
                } else if (j == 9) {
                    sum = dp[i-1][j-1];
                } else {
                    sum = dp[i-1][j-1] + dp[i-1][j+1];
                }
                dp[i][j] = sum % div;
            }
        }

        for (int i = 0; i < 10; i++) {
            result = (result + dp[N][i]) % div;
        }

        System.out.println(result);
    }
}