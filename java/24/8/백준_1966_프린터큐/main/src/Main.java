import java.util.*;
import java.io.*;

public class Main {
    static int t, n, m;
    static LinkedList<int[]> queue;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        t = Integer.parseInt(st.nextToken());

        for (int i = 0; i < t; i ++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            queue = new LinkedList<>();

            for (int j = 0; j < n; j ++) {
                queue.add(new int[] {j, Integer.parseInt(st.nextToken())} );
            }
            solve(n, m, queue);
        }

        System.out.println(sb);
    }

    static void solve(int n, int m, LinkedList<int[]> queue) {
        int cnt = 0;
        while (!queue.isEmpty()) {
            int[] front = queue.poll();
            boolean isMax = true;

            for (int i = 0; i < queue.size(); i++) {
                if (front[1] < queue.get(i)[1]) {
                    isMax = false;
                    break;
                }
            }
            if (!isMax) {
                queue.offer(front);
                continue;
            }

            cnt ++;
            if (front[0] == m) {
                sb.append(cnt + "\n");
                break;
            }
        }
    }
}