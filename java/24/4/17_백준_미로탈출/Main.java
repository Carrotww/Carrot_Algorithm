// https://www.acmicpc.net/problem/14923

import java.io.*;
import java.util.*;

public class Main {
    static int[][] graph;
    static int[][][] visited;
    static int r, c, startR, startC, targetR, targetC;
    static int result = Integer.MAX_VALUE;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};
    static Queue<Info> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] rc = br.readLine().split(" ");
        r = Integer.parseInt(rc[0]);
        c = Integer.parseInt(rc[1]);

        String[] start = br.readLine().split(" ");
        startR = Integer.parseInt(start[0]) - 1;
        startC = Integer.parseInt(start[1]) - 1;

        String[] target = br.readLine().split(" ");
        targetR = Integer.parseInt(target[0]) - 1;
        targetC = Integer.parseInt(target[1]) - 1;

        graph = new int[r][c];
        visited = new int[r][c][2];

        for (int i = 0; i < r; i++) {
            String[] t = br.readLine().split(" ");
            for (int j = 0; j < c; j++) {
                graph[i][j] = Integer.parseInt(t[j]);
            }
        }

        queue.offer(new Info (startR, startC, 0, 0));
        visited[startR][startC][0] = 1;

        while (!queue.isEmpty()) {
            Info info = queue.poll();
            
            if (info.r == targetR && info.c == targetC) {
                result = info.cnt;
                break;
            }

            for (int d = 0; d < 4; d++) {
                int nr = info.r + dr[d];
                int nc = info.c + dc[d];
                if ((nr < 0 || nr >= r) || (nc < 0 || nc >= c)) {
                    continue;
                }
                if (visited[nr][nc][info.isBroken] == 1) {
                    continue;
                }
                if (graph[nr][nc] == 1 && info.isBroken == 0) {
                    queue.offer(new Info (nr, nc, 1, info.cnt+1));
                    visited[nr][nc][1] = 1;
                } else if (graph[nr][nc] == 0) {
                    queue.offer(new Info (nr, nc, info.isBroken, info.cnt+1));
                    visited[nr][nc][info.isBroken] = 1;
                }
            }
        }

        if (result == Integer.MAX_VALUE) {
            System.out.println("-1");
        } else {
            System.out.println(result);
        }
    }

    public static class Info {
        int r, c, isBroken, cnt;
        public Info(int r, int c, int isBroken, int cnt) {
            this.r = r;
            this.c = c;
            this.isBroken = isBroken;
            this.cnt = cnt;
        }
    }
}

