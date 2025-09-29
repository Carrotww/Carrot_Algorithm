/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 16918                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/16918                          #+#        #+#      #+#    */
/*   Solved: 2025/09/29 21:49:25 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    static int R;
    static int C;
    static int[][] graph;
    static int time;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        time = Integer.parseInt(st.nextToken());

        graph = new int[R][C];

        for (int r = 0; r < R; r++) {
            String line = br.readLine();
            for (int c = 0; c < C; c++) {
                if (line.charAt(c) == '.')
                    graph[r][c] = 0;
                else
                    graph[r][c] = 1;
            }
        }

        for (int t = 2; t <= time; t++) {
            // 1) 모든 기존 폭탄 나이 +1
            boomPlusTime(1, graph);

            if (t % 2 == 0) {
                // 2) 짝수초: 빈칸 전부 설치(나이 1)
                boomSetting(graph);
            } else {
                // 3) 홀수초(3,5,7...): 나이==3만 동시 폭발
                boomGraph(graph);
            }
        }

        // 결과 호출
        printResult(graph);
    }

    public static void printResult(int[][] graph) {
        StringBuilder sb = new StringBuilder();

        for (int[] gg : graph) {
            for (int g : gg) {
                if (g == 0) {
                    sb.append(".");
                } else {
                    sb.append("O");
                }
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

    public static void boomPlusTime(int cnt, int[][] graph) {
        for (int r = 0; r < graph.length; r++) {
            for (int c = 0; c < graph[0].length; c++) {
                if (graph[r][c] != 0) {
                    graph[r][c] += cnt;
                }
            }
        }
    }

    public static void boomGraph(int[][] graph) {
        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};

        boolean[][] clear = new boolean[graph.length][graph[0].length];

        for (int r = 0; r < graph.length; r++) {
            for (int c = 0; c < graph[0].length; c++) {
                if (graph[r][c] == 3) { // 설치 후 3초 지난 폭탄만 폭발
                    clear[r][c] = true;
                    for (int d = 0; d < 4; d++) {
                        int nr = r + dr[d], nc = c + dc[d];
                        if (nr < 0 || nr >= graph.length || nc < 0 || nc >= graph[0].length) continue;
                        clear[nr][nc] = true;
                    }
                }
            }
        }

        // ★ 일괄 삭제
        for (int r = 0; r < graph.length; r++) {
            for (int c = 0; c < graph[0].length; c++) {
                if (clear[r][c]) graph[r][c] = 0;
            }
        }
    }

    public static void boomSetting(int[][] graph) {
        for (int r = 0; r < graph.length; r++) {
            for (int c = 0; c < graph[0].length; c++) {
                if (graph[r][c] == 0) {
                    graph[r][c] = 1;
                }
            }
        }
    }
}