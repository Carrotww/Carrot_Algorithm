/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1347                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1347                           #+#        #+#      #+#    */
/*   Solved: 2025/09/23 23:07:44 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        String line = br.readLine();

        final int SIZE = 101;
        final int MID = SIZE / 2;

        // 101 * 101 로 크게 잡고
        boolean[][] visited = new boolean[SIZE][SIZE];

        int r = MID;
        int c = MID;
        int d = 0; // down

        int maxR = r;
        int minR = r;
        int maxC = c;
        int minC = c;

        int[] dr = new int[] {1, 0, -1, 0};
        int[] dc = new int[] {0, -1, 0, 1};

        visited[r][c] = true;

        for (int i = 0; i < N; i++) {
            char command = line.charAt(i);

            if (command == 'F') {
                r += dr[d];
                c += dc[d];
                visited[r][c] = true;

                maxR = Math.max(maxR, r);
                minR = Math.min(minR, r);
                maxC = Math.max(maxC, c);
                minC = Math.min(minC, c);
            }
            else if (command == 'L') d = (d + 3) % 4;

            else if (command == 'R') d = (d + 1) % 4;
        }

        StringBuilder sb = new StringBuilder();

        for (int i = minR; i <= maxR; i++) {
            for (int j = minC; j <= maxC; j++) {
                sb.append(visited[i][j] ? '.' : '#');
            }
            sb.append('\n');
        }

        System.out.println(sb);
    }
}