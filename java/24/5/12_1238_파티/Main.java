// https://www.acmicpc.net/problem/1238

import java.io.*;
import java.util.*;

class Info implements Comparable<Info> {
    int end;
    int time;

    Info(int end, int time) {
        this.end = end;
        this.time = time;
    }

    @Override
    public int compareTo(Info o) {
        return this.time - o.time;
    }
}

public class Main {
    static int n;
    static int m;
    static int x;
    static ArrayList<ArrayList<Info>> graph;
    static int[][] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);
        x = Integer.parseInt(input[2]);

        graph = new ArrayList<>(n+1);

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int start, end, time;
            String[] input2 = br.readLine().split(" ");
            start = Integer.parseInt(input2[0]);
            end = Integer.parseInt(input2[1]);
            time = Integer.parseInt(input2[2]);
            graph.get(start).add(new Info(end, time));
        }

    }

    public static void dj() {

    }
}


