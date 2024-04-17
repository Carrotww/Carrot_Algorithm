// https://www.acmicpc.net/problem/14923

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String []args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] rc = br.readLine().split(" ");
        int r = Integer.parseInt(rc[0]);
        int c = Integer.parseInt(rc[1]);

        String[] start = br.readLine().split(" ");
        int startR = Integer.parseInt(start[0]);
        int startC = Integer.parseInt(start[1]);

        String[] target = br.readLine().split(" ");
        int targetR = Integer.parseInt(target[0]);
        int targetC = Integer.parseInt(target[1]);

        int[][] graph = new int[r][c];
        for (int i = 0; i < r; i++) {
            String[] t = br.readLine().split(" ");
            for (int j = 0; j < c; j++) {
                graph[i][j] = Integer.parseInt(t[j]);
            }
        }
    }
}
