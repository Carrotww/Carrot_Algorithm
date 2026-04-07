/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1915                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1915                           #+#        #+#      #+#    */
/*   Solved: 2026/03/18 20:52:50 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] graph = new int[n][m];

        for (int i = 0; i < n; i++) {
            String input = br.readLine().strip();

            int cnt = 0;
            for (char c : input.toCharArray()) {
                graph[i][cnt++] = c - '0';
            }
        }

        int[][] dp = new int[n][m];

        for (int i = 0; i < n; i++) {
            dp[i][0] = graph[i][0] == 1 ? 1 : 0;
        }

        for (int j = 0; j < m; j++) {
            dp[0][j] = graph[0][j] == 1 ? 1 : 0;
        }

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                dp[i][j] = graph[i][j] == 1 ? Math.min(Math.min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]) + 1 : 0;
            }
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                result = Math.max(result, dp[i][j]);
            }
        }

        System.out.println(result * result);
    }

    public static void printlist(int[][] graph) {
        for (int i = 0; i < graph.length; i++) {
            for (int j = 0; j < graph[0].length; j++) {
                System.out.print(graph[i][j] + " ");
            }
            System.out.println();
        }
    }
}