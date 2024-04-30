// https://www.acmicpc.net/problem/2660

import java.util.*;
import java.io.*;
import java.lang.Math;

public class Main {
    static int n;
    static int[][] graph;
    static int INF = 50;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        graph = new int[n+1][n+1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == j) {
                    continue;
                }
                graph[i][j] = INF;
            }
        }

        while (true) {
            String[] input = br.readLine().split(" ");
            int a = Integer.parseInt(input[0]);
            int b = Integer.parseInt(input[1]);

            if (a == -1 && b == -1) {
                break;
            }
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        fw();

        for (int[] row : graph) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }

        int memberMinValue = INF;
        int total = 0;
        int[] memberList = new int[n];

        for (int node = 1; node <= n; node++) {
            int curMemberMaxValue = 0;
            for (int i = 1; i <= n; i++) {
                curMemberMaxValue = Math.max(curMemberMaxValue, graph[node][i]);
            }
            memberMinValue = Math.min(curMemberMaxValue, memberMinValue);
        }

        System.out.println(memberMinValue);
    }

    public static void fw() {
        for (int node = 1; node <= n; node ++) {
            for (int a = 1; a <= n; a ++) {
                for (int b = 1; b <= n; b ++) {
                    graph[a][b] = Math.min(graph[a][node] + graph[node][b], graph[a][b]);
                }
            }
        }
    }
}

