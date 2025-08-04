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

public class Main2 {

    static int N, M;
    static int[][] graph;
    static boolean[][] visited;
    static ArrayList<int[]>[][] lights;
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        input();

        // 0, 0부터 큐에 넣고 불 켜고 bfs 돌리자
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {0, 0});
        graph[0][0] = 1;
        visited[0][0] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0];
            int c = cur[1];

            for (int[] light : lights[r][c]) {
                // 하나씩 불 켜주고 불 켜진곳이 아직 방문 안되어 있으면 4방향 확인해서 거기를 큐에 넣어준다.
                int curR = light[0];
                int curC = light[1];

                if (graph[curR][curC] == 0 && !visited[curR][curC]) {
                    for (int d = 0; d < 4; d++) {
                        int nR = curR + dr[d];
                        int nC = curC + dc[d];

                        if (isRange(nR, nC) && visited[nR][nC]) {
                            q.add(new int[] {nR, nC});
                        }
                    }
                }
                graph[curR][curC] = 1;
            }

            for (int d = 0; d < 4; d++) {
                int nR = r + dr[d];
                int nC = c + dc[d];

                if (isRange(nR, nC) && !visited[nR][nC] && graph[nR][nC] == 1) {
                    q.add(new int[] {nR, nC});
                    visited[nR][nC] = true;
                }
            }
        }

        int result = 0;

        for (int[] ary : graph) {
            result += Arrays.stream(ary).sum();
        }

        System.out.println(result);
    }

    public static boolean isRange(int r, int c) {
        if (r < 0 || r >= N || c < 0 || c >= N) return false;
        else return true;
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
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            lights[x][y].add(new int[]{a, b});
        }
    }
}