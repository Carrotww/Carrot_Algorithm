// https://www.acmicpc.net/problem/7562
import java.util.*;
import java.io.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static int n;
    private static int target_r;
    private static int target_c;

    public static void main(String[] args) throws IOException {
        String t = br.readLine();

        for (int i = 0; i < Integer.parseInt(t); i++) {
            solve();
        }
    }

    private static void solve() throws IOException {
        n = Integer.parseInt(br.readLine());
        String input = br.readLine();
        String[] curValue = input.split(" ");
        int cur_r = Integer.parseInt(curValue[0]);
        int cur_c = Integer.parseInt(curValue[1]);

        String input2 = br.readLine();
        String[] targetValue = input2.split(" ");
        target_r = Integer.parseInt(targetValue[0]);
        target_c = Integer.parseInt(targetValue[1]);

        System.out.println(bfs(cur_r, cur_c));
    }

    private static int bfs(int r, int c) {
        Queue<int[]> queue = new LinkedList<>();
        int[][] visited = new int[n][n];
        int[][] moves = {
            {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2},
            {1, 2}, {2, 1}, {2, -1}, {1, -2}
        };
        for (int i = 0; i < n; i++) {
            Arrays.fill(visited[i], -1);
        }
        queue.offer(new int[]{r, c});
        if ((r == target_r) && (c == target_c)) {
            return 0;
        }
        int result = 0;
        visited[r][c] = 0;

        while (queue.size() > 0) {
            int[] cur_val = queue.poll();
            int cur_r = cur_val[0];
            int cur_c = cur_val[1];

            for (int[] move : moves) {
                int n_r = cur_r + move[0];
                int n_c = cur_c + move[1];
                if (n_r == target_r && n_c == target_c) {
                    return visited[cur_r][cur_c] + 1;
                }
                if ((n_r < 0 || n_r >= n) || (n_c < 0 || n_c >= n) || (visited[n_r][n_c] != -1)) {
                    continue;
                } else {
                    visited[n_r][n_c] = visited[cur_r][cur_c] + 1;
                    queue.offer(new int[] {n_r, n_c});
                }
            }
        }
        return -1;
    }
}

