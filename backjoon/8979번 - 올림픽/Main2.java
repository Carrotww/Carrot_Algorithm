import java.io.*;
import java.util.*;

public class Main2 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] g = new int[N + 1];
        int[] s = new int[N + 1];
        int[] b = new int[N + 1];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int id = Integer.parseInt(st.nextToken());
            g[id] = Integer.parseInt(st.nextToken());
            s[id] = Integer.parseInt(st.nextToken());
            b[id] = Integer.parseInt(st.nextToken());
        }

        int rk = 1;
        for (int i = 1; i <= N; i++) {
            if (g[i] > g[K] ||
               (g[i] == g[K] && s[i] > s[K]) ||
               (g[i] == g[K] && s[i] == s[K] && b[i] > b[K])) {
                rk++;
            }
        }
        System.out.println(rk);
    }
}
