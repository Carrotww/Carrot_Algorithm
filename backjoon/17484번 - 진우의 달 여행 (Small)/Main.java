/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 17484                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/17484                          #+#        #+#      #+#    */
/*   Solved: 2025/08/28 21:06:56 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

class Rocket {
    int r;
    int c;
    int fuel;
    int prevMove;

    Rocket(int r, int c, int fuel, int prevMove) {
        this.r = r;
        this.c = c;
        this.fuel = fuel;
        this.prevMove = prevMove;
    }

    @Override
    public String toString() {
        return "{" + r + " " + c + " " + fuel + "}";
    }
}

public class Main {

    static int N;
    static int M;
    static int[][] graph;
    static int[] dr = new int[] { 1, 1, 1 };
    static int[] dc = new int[] { -1, 0, 1 };

    public static void main(String[] args) throws IOException {
        input();

        // init append queue
        Queue<Rocket> q = new LinkedList<>();

        for (int i = 0; i < M; i++) {
            q.add(new Rocket(0, i, graph[0][i], -1));
        }
        
        int result = Integer.MAX_VALUE;

        while (!q.isEmpty()) {
            Rocket curRocket = q.poll();

            if (curRocket.r == N - 1) {
                result = Math.min(result, curRocket.fuel);
                continue;
            }

            for (int d = 0; d < 3; d++) {
                int nR = curRocket.r + dr[d];
                int nC = curRocket.c + dc[d];

                if (nR >= N || nC >= M || nC < 0 || curRocket.prevMove == d) continue;

                q.add(new Rocket(nR, nC, curRocket.fuel + graph[nR][nC], d));
            }
        }

        System.out.println(result);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new int[N][M];

        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < M; c++) {
                graph[r][c] = Integer.parseInt(st.nextToken());
            }
        }
    }
}