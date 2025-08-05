/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2933                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2933                           #+#        #+#      #+#    */
/*   Solved: 2025/08/05 09:13:19 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

// r, c - graph no blank - list

import java.util.*;
import java.io.*;

public class Main {

    static int R;
    static int C;
    static int M;
    static char[][] graph;
    static int[][] visited;
    static int[] stoneAry; // 짝수는 왼쪽 홀수는 오른쪽
    static int[] dr = new int[] { 1, -1, 0, 0 };
    static int[] dc = new int[] { 0, 0, 1, -1 };
    static int visiteCnt = 1;

    static int cnt = 0;

    public static void main(String[] args) throws IOException {
        input();

        for (int m = 0; m < M; m++) {
            int curHeight = R - stoneAry[m];
            int curCol;

            if (m % 2 == 0) {
                // 왼쪽
                curCol = 0;
                while (graph[curHeight][curCol] != 'x' && curCol < C - 1) {
                    curCol++;
                }

            } else {
                // 오른쪽
                curCol = C - 1;
                while (graph[curHeight][curCol] != 'x' && curCol > 0) {
                    curCol--;
                }

            }

            if (graph[curHeight][curCol] == 'x') {
                graph[curHeight][curCol] = '.';

                // bfs + cluster down
                bfs();
            } else {
                continue;
            }

            // printGraph();
        }

        StringBuffer sb = new StringBuffer();
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                sb.append(graph[r][c]);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    public static void bfs() {
        visited = new int[R][C];

        for (int r = R - 2; r >= 0; r--) {
            for (int c = 0; c < C; c++) {
                if (visited[r][c] == 0 && graph[r][c] == 'x') {
                    Queue<int[]> q = new LinkedList();
                    q.add(new int[] { r, c });
                    visited[r][c] = visiteCnt;
                    // isUp flag를 true로 설정 후 row값이 하나라도 바닥(R-1)에 있다면 false로 바꾸어 준다.
                    boolean isUp = true;

                    while (!q.isEmpty()) {
                        int[] node = q.poll();
                        int curR = node[0];
                        int curC = node[1];

                        if (curR == R - 1)
                            isUp = false;

                        for (int d = 0; d < 4; d++) {
                            int nR = curR + dr[d];
                            int nC = curC + dc[d];

                            if (nR < 0 || nR >= R || nC < 0 || nC >= C)
                                continue;

                            if (visited[nR][nC] == 0 && graph[nR][nC] == 'x') {
                                q.add(new int[] { nR, nC });
                                visited[nR][nC] = visiteCnt;
                            }
                        }
                    }

                    if (isUp) {
                        // 모양 그대로 떨어뜨리기
                        downCluster(visiteCnt);
                    }

                    visiteCnt++;
                }
            }
        }
    }

    public static void downCluster(int cnt) {

        int minMove = R;

        for (int c = 0; c < C; c++) {
            for (int r = R - 1; r >= 0; r--) {
                if (visited[r][c] == cnt) {
                    int nR = r + 1;
                    while (nR < R && visited[nR][c] != cnt && graph[nR][c] == '.') {
                        nR++;
                    }

                    minMove = Math.min(minMove, nR - r - 1);
                    break;
                }
            }
        }

        List<int[]> cluster = new ArrayList<>();
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (visited[r][c] == cnt) {
                    cluster.add(new int[] { r, c });
                    graph[r][c] = '.';
                    visited[r][c] = 0;
                }
            }
        }

        for (int[] pos : cluster) {
            int nR = pos[0] + minMove;
            int nC = pos[1];
            graph[nR][nC] = 'x';
            visited[nR][nC] = cnt;
        }
    }

    public static void printGraph() {
        System.out.println("=========" + cnt + "=========");
        for (char[] g : graph) {
            System.out.println(Arrays.toString(g));
        }
        System.out.println("========================");
        cnt++;
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        graph = new char[R][C];

        for (int r = 0; r < R; r++) {
            String line = br.readLine();
            for (int c = 0; c < C; c++) {
                graph[r][c] = line.charAt(c);
            }
        }

        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        stoneAry = new int[M];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            stoneAry[i] = Integer.parseInt(st.nextToken());
        }
    }
}