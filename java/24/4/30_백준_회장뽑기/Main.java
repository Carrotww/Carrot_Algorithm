// https://www.acmicpc.net/problem/2660

import java.util.*;
import java.io.*;
import java.lang.Math;

public class Main {
    static int n;
    static int[][] graph;
    static int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        graph = new int[n+1][n+1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == j) {
                    graph[i][j] = 0;
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

        int memberMinValue = INF;
        int[] memberList = new int[n+1];
        ArrayList<Integer> candidate = new ArrayList<>();

        for (int node = 1; node <= n; node++) {
            int curMemberMaxValue = 0;
            for (int i = 1; i <= n; i++) {
                curMemberMaxValue = Math.max(curMemberMaxValue, graph[node][i]);
            }
            memberList[node] = curMemberMaxValue;
            memberMinValue = Math.min(curMemberMaxValue, memberMinValue);
        }

        for (int node = 1; node <= n; node ++) {
            if (memberList[node] == memberMinValue) {
                candidate.add(node);
            }
        }

        System.out.println(memberMinValue + " " + candidate.size());
        for (int c : candidate) {
            System.out.print(c + " ");
        }
    }

    public static void fw() {
        for (int node = 1; node <= n; node ++) {
            for (int a = 1; a <= n; a ++) {
                for (int b = 1; b <= n; b ++) {
                    if (graph[a][node] == INF || graph[node][b] == INF) {
                        continue;
                    }
                    graph[a][b] = Math.min(graph[a][node] + graph[node][b], graph[a][b]);
                }
            }
        }
    }
}

