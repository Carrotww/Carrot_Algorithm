/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1018                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1018                           #+#        #+#      #+#    */
/*   Solved: 2025/09/25 17:11:55 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {

    static int[][] graph; // input
    static int R;
    static int C;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        graph = new int[R][C];

        for (int r = 0; r < R; r++) {
            String line = br.readLine();
            for (int c = 0; c < C; c++) {

                if (line.charAt(c) == 'B') {
                    graph[r][c] = 1;
                } else {
                    graph[r][c] = -1;
                }
            }
        }

        // 50 * 50 = 2500
        // 전부 비교하면 될 것 같다 한칸 씩 옮기면서

        int result = 8 * 8;

        for (int i = 0; i <= R - 8; i++) {
            for (int j = 0; j <= C - 8; j++) {
                // 함수 호출
                result = Math.min(compareGraph(i, j, 1), result);
                result = Math.min(compareGraph(i, j, -1), result);
            }
        }

        System.out.println(result);
    }

    public static int compareGraph(int startR, int startC, int color) {
        // 왼쪽 위 부터 비교하기
        int cnt = 0;

        for (int r = 0; r < 8; r++) {
            for (int c = 0; c < 8; c++) {
                if (graph[r + startR][c + startC] != color) cnt++;
                color *= -1;
            }
            color *= -1;
        }

        return cnt;
    }
}