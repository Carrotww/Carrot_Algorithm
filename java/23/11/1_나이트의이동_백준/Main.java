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

        bfs(cur_r, cur_c);
    }

    private static int bfs(int r, int c) {
        List<Integer> queue = new LinkedList<>();
        int[][] visited = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(visited[i], -1);
        }

        return 0;
    }
}
