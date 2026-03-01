/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1743                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1743                           #+#        #+#      #+#    */
/*   Solved: 2026/02/25 21:31:45 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R, C, K;

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        // dfs 로 풀어보기

        int result = 0;

        int[][] graph = new int[R][C];

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;

            graph[r][c] = 1;
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                result = Math.max(result, dfs(graph, R, C, i, j));
            }
        }

        System.out.println(result);
    }

    public static int dfs(int[][] graph, int R, int C, int r, int c) {
        int[] dr = new int[] {1, -1, 0, 0};
        int[] dc = new int[] {0, 0, 1, -1};

        if (graph[r][c] == 0) {
            return 0;
        }

        graph[r][c] = 0;
        int cnt = 1;

        for (int d = 0; d < 4; d++) {
            int nr = dr[d] + r;
            int nc = dc[d] + c;

            if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;

            if (graph[nr][nc] == 1) {
                cnt += dfs(graph, R, C, nr, nc);
            }
        }

        return cnt;
    }
}