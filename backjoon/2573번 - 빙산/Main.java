/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2573                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2573                           #+#        #+#      #+#    */
/*   Solved: 2026/03/26 22:02:01 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        int[][] graph = new int[R][C];
        int[][] visited = new int[R][C];

        for (int r = 0; r < R; r++) {
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < C; i++) {
                graph[r][i] = Integer.parseInt(st.nextToken());
            }
        }

        int total = 0;
        int cnt;

        while (true) {
            cnt = bfs(R, C, visited, graph);

            if (cnt > 1) {
                System.out.println(total);
                break;
            }

            if (cnt == 0) {
                System.out.println(0);
                break;
            }

            melt(R, C, visited, graph);
            total++;
        }

        // melt(R, C, visited, graph);

        // for (int i = 0; i < R; i++) {
        //     System.out.println(Arrays.toString(graph[i]));
        // }
    }

    public static int bfs(int R, int C, int[][] visited, int[][] graph) {
        Deque<int[]> q = new ArrayDeque<>();
        visited = new int[R][C];

        int[] dr = new int[] {1, -1, 0, 0};
        int[] dc = new int[] {0, 0, 1, -1};
        int cnt = 0;

        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (visited[r][c] == 0 && graph[r][c] != 0) {
                    cnt++;
                    if (cnt > 1) return cnt;

                    q.add(new int[] {r, c});
                    visited[r][c] = 1;

                    while (!q.isEmpty()) {
                        int[] cur = q.poll();
                        int curR = cur[0];
                        int curC = cur[1];

                        for (int d = 0; d < 4; d++) {
                            int nR = curR + dr[d];
                            int nC = curC + dc[d];

                            if (nR < 0 || nR >= R || nC < 0 || nC >= C) continue;

                            if (visited[nR][nC] == 0 && graph[nR][nC] != 0) {
                                visited[nR][nC] = 1;
                                q.add(new int[] {nR, nC});
                            }
                        }
                    }
                }
            }
        }

        return cnt;
    }

    public static void melt(int R, int C, int[][] visited, int[][] graph) {
        int[] dr = new int[] {1, -1, 0, 0};
        int[] dc = new int[] {0, 0, 1, -1};

        visited = new int[R][C];

        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (graph[r][c] != 0) {
                    for (int d = 0; d < 4; d++) {
                        int nr = r + dr[d];
                        int nc = c + dc[d];

                        if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;

                        if (graph[nr][nc] == 0) visited[r][c]++;
                    }
                }
            }
        }

        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (visited[r][c] > 0) {
                    int value = graph[r][c] - visited[r][c];
                    graph[r][c] = (value < 0) ? 0 : value;
                }
            }
        }
    }
}
