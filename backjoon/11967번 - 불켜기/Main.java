/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 11967                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/11967                          #+#        #+#      #+#    */
/*   Solved: 2025/08/03 17:23:07 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 11967                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/11967                          #+#        #+#      #+#    */
/*   Solved: 2025/08/03 17:23:07 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {

    static int N, M;
    static int[][] graph;
    static boolean[][] visited;
    static ArrayList<int[]>[][] lights;
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        input();

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {0, 0});
        graph[0][0] = 1;
        visited[0][0] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1];

            // 스위치 작동
            for (int[] light : lights[r][c]) {
                int lr = light[0] - 1;
                int lc = light[1] - 1;

                // 아직 불이 꺼져있다면
                if (graph[lr][lc] == 0) {
                    graph[lr][lc] = 1;

                    // 불 켜진 방 주변에 방문된 곳이 있다면 즉시 큐에 넣음
                    for (int d = 0; d < 4; d++) {
                        int nr = lr + dr[d];
                        int nc = lc + dc[d];
                        if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

                        if (visited[nr][nc]) {
                            q.add(new int[]{lr, lc});
                            visited[lr][lc] = true;
                        }
                    }
                }
            }

            // 현재 위치에서 4방향 이동
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
                if (graph[nr][nc] == 1 && !visited[nr][nc]) {
                    q.add(new int[]{nr, nc});
                    visited[nr][nc] = true;
                }
            }
        }

        // 불 켜진 방 개수 세기
        int result = 0;
        for (int[] row : graph) {
            for (int cell : row) {
                result += cell;
            }
        }

        System.out.println(result);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new int[N][N];
        visited = new boolean[N][N];
        lights = new ArrayList[N][N];

        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                lights[i][j] = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            lights[x][y].add(new int[]{a, b});
        }
    }
}
