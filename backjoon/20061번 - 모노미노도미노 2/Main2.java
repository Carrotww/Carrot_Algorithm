/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 20061                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/20061                          #+#        #+#      #+#    */
/*   Solved: 2025/09/11 23:06:17 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main2 {
    // x = row, y = col
    // t = 1 -> (x, y)
    // t = 2 -> (x, y), (x, y + 1)
    // t = 3 -> (x, y), (x + 1, y)

    static boolean[][] graph = new boolean[10][10];
    static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            // 움직여주기
            moveBlue(t, r);
            moveGreen(t, c);

            // 터뜨리기, 터졌으면 움직이기 터지면 점수
            popBlue();
            popGreen();

            // 경계 확인해서 밀어주기
            checkBlueLine();
            checkGreenLine();
        }

        int cnt = 0;

        for (int r = 6; r < 10; r++)
            for (int c = 0; c < 4; c++)
                if (graph[r][c])
                    cnt++;

        for (int c = 6; c < 10; c++)
            for (int r = 0; r < 4; r++)
                if (graph[r][c])
                    cnt++;

        System.out.println(result);
        System.out.println(cnt);
    }

    public static void moveGreen(int t, int c) {
        // 아래로 내려감

        int r = 0;

        if (t == 1) { // (r, c)
            while (r + 1 < 10 && !graph[r + 1][c])
                r++;

            graph[r][c] = true;

        } else if (t == 2) { // (r, c), (r, c + 1)
            while (r + 1 < 10 && !graph[r + 1][c] && !graph[r + 1][c + 1])
                r++;

            graph[r][c] = graph[r][c + 1] = true;

        } else if (t == 3) { // (r, c), (r + 1, c)
            while (r + 2 < 10 && !graph[r + 2][c])
                r++;

            graph[r][c] = graph[r + 1][c] = true;
        }
    }

    public static void moveBlue(int t, int r) {
        // 오른쪽으로 감

        int c = 0;

        if (t == 1) { // (r, c)
            while (c + 1 < 10 && !graph[r][c + 1])
                c++;
            graph[r][c] = true;

        } else if (t == 2) { // (r, c), (r, c + 1) 가로
            while (c + 2 < 10 && !graph[r][c + 2])
                c++;

            graph[r][c] = graph[r][c + 1] = true;

        } else if (t == 3) { // (r, c), (r + 1, c) 세로
            while (c + 1 < 10 && !graph[r][c + 1] && !graph[r + 1][c + 1])
                c++;

            graph[r][c] = graph[r + 1][c] = true;
        }
    }

    public static void popGreen() {
        // 터뜨리고 터지면 밀어 줌
        for (int r = 9; r >= 4;) {
            boolean canPop = true;

            for (int c = 0; c < 4; c++)
                if (!graph[r][c]) {
                    canPop = false;
                    break;
                }

            if (canPop) {
                // 터뜨려 주기
                for (int c = 0; c < 4; c++)
                    graph[r][c] = false;

                for (int mr = r; mr > 3; mr--)
                    for (int c = 0; c < 4; c++)
                        graph[mr][c] = graph[mr - 1][c];

                result++;
            } else r--;
        }
    }

    public static void popBlue() {
        for (int c = 9; c >= 4;) {
            boolean canPop = true;

            for (int r = 0; r < 4; r++)
                if (!graph[r][c]) {
                    canPop = false;
                    break;
                }

            if (canPop) {
                for (int r = 0; r < 4; r++)
                    graph[r][c] = false;

                for (int mc = c; mc > 3; mc--)
                    for (int r = 0; r < 4; r++)
                        graph[r][mc] = graph[r][mc - 1];

                result++;
            } else c--;
        }
    }

    public static void checkGreenLine() {
        // r = 4, 5

        int push = 0;

        for (int r = 4; r < 6; r++)
            for (int c = 0; c < 4; c++)
                if (graph[r][c]) {
                    push++;
                    break;
                }

        // r = 9 ~ 4
        while (push-- > 0) {
            for (int c = 0; c < 4; c++)
                graph[9][c] = false;

            for (int r = 9; r >= 4; r--)
                for (int c = 0; c < 4; c++) {
                    graph[r][c] = graph[r - 1][c];
                    graph[r - 1][c] = false;
                }
        }
    }

    public static void checkBlueLine() {
        // c = 4, 5

        int push = 0;

        for (int c = 4; c < 6; c++)
            for (int r = 0; r < 4; r++)
                if (graph[r][c]) {
                    push++;
                    break;
                }

        while (push-- > 0) {
            for (int r = 0; r < 4; r++)
                graph[r][9] = false;

            for (int c = 9; c >= 4; c--)
                for (int r = 0; r < 4; r++) {
                    graph[r][c] = graph[r][c - 1];
                    graph[r][c - 1] = false;
                }
        }
    }
}