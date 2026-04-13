
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        int[][] graph = new int[R][C];
        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] dp = new int[R][C];
        dp[0][0] = graph[0][0];

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                // 왼쪽
                if (j > 0) {
                    dp[i][j] = Math.max(dp[i][j], graph[i][j] + dp[i][j - 1]);
                }

                // 왼쪽 위 대각선
                if (i > 0 && j > 0) {
                    dp[i][j] = Math.max(dp[i][j], graph[i][j] + dp[i - 1][j - 1]);
                }

                // 위
                if (i > 0) {
                    dp[i][j] = Math.max(dp[i][j], graph[i][j] + dp[i - 1][j]);
                }
            }
        }

        System.out.println(dp[R - 1][C - 1]);
    }
}
