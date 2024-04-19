import java.io.*;
import java.util.*;

public class Main2 {
    static int r, c, startR, startC, targetR, targetC;
    static int[][] graph;
    static int[][][] visited;
    static int result = Integer.MAX_VALUE;
    static int[] dr = {0, -1, 0, 1};
    static int[] dc = {1, 0, -1, 0};
    static Queue<Info> queue = new LinkedList<>();

    public static class Info{
        int curR, curC, isBroken, cnt;
        public Info(int curR, int curC, int isBroken, int cnt) {
            this.curR = curR;
            this.curC = curC;
            this.isBroken = isBroken;
            this.cnt = cnt;
        }
    }

    public static int bfs() {
        queue.offer(new Info(startR, startC, 0, 0));
        visited = new int[r][c][2];
        visited[startR][startC][0] = 1;

        while (!queue.isEmpty()) {
            Info info = queue.poll();
            // System.out.println(info.curR + " " + info.curC + " " + info.isBroken + " " + info.cnt);
            if (info.curR == targetR && info.curC == targetC) {
                return info.cnt;
            }

            for (int d = 0; d < 4; d++) {
                int nr = info.curR + dr[d];
                int nc = info.curC + dc[d];

                if ((nr < 0 || nr >= r) || (nc < 0 || nc >= c)) {
                    continue;
                }
                if (visited[nr][nc][info.isBroken] == 1) {
                    continue;
                }
                if (graph[nr][nc] == 1 && info.isBroken == 0) {
                    queue.offer(new Info(nr, nc, 1, info.cnt+1));
                    visited[nr][nc][1] = 1;
                } else if (graph[nr][nc] == 0){
                    queue.offer(new Info(nr, nc, info.isBroken, info.cnt+1));
                    visited[nr][nc][info.isBroken] = 1;
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] t = br.readLine().split(" ");
        r = Integer.parseInt(t[0]);
        c = Integer.parseInt(t[1]);

        String[] tt = br.readLine().split(" ");
        startR = Integer.parseInt(tt[0]) - 1;
        startC = Integer.parseInt(tt[1]) - 1;

        String[] ttt = br.readLine().split(" ");
        targetR = Integer.parseInt(ttt[0]) - 1;
        targetC = Integer.parseInt(ttt[1]) - 1;

        graph = new int[r][c];
        for (int i = 0; i < r; i++) {
            String[] tttt = br.readLine().split(" ");
            for (int j = 0; j < c; j++) {
                graph[i][j] = Integer.parseInt(tttt[j]);
            }
        }

        int result = bfs();
        System.out.println(result);
    }
}

