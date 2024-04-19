// https://www.acmicpc.net/problem/21278

import java.io.*;
import java.util.*;

public class Main {
    static int n, m, aBuilding, bBuilding, result;
    static int[][] graph;
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] nm = br.readLine().split(" ");
        n = Integer.parseInt(nm[0]);
        m = Integer.parseInt(nm[1]);

        graph = new int[n+1][n+1];

        for (int i = 0; i <= n; i++) {
            Arrays.fill(graph[i], INF);
            graph[i][i] = 0;
        }

        for (int i = 0; i < m; i++) {
            String[] ab = br.readLine().split(" ");
            int a, b;
            a = Integer.parseInt(ab[0]);
            b = Integer.parseInt(ab[1]);
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (graph[i][k] != INF && graph[k][j] != INF) {
                        graph[i][j] = Math.min(graph[i][k] + graph[k][j], graph[i][j]);
                    }
                }
            }
        }

        aBuilding = -1;
        bBuilding = -1;
        result = INF;

        for (int i = 1; i < n; i++) {
            for (int j = i+1; j <= n; j++) {
                int curTotal = 0;
                for (int node = 1; node <= n; node++) {
                    curTotal += Math.min(graph[i][node] * 2, graph[j][node] * 2);
                }
                if (curTotal < result) {
                    result = curTotal;
                    aBuilding = i;
                    bBuilding = j;
                }
            }
        }

        System.out.println(aBuilding + " " + bBuilding + " " + result);
    }
}

