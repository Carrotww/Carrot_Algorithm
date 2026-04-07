/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1647                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1647                           #+#        #+#      #+#    */
/*   Solved: 2026/04/07 21:55:00 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        List<int[]> edges = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            edges.add(new int[] {start, end, cost});
        }

        edges.sort(Comparator.comparingInt(x -> x[2]));

        int lastCost = 0;
        int total = 0;
        int[] parents = new int[N + 1];
        for (int i = 0; i < N + 1; i++) parents[i] = i;

        for (int[] edge : edges) {
            int start = edge[0];
            int end = edge[1];
            int cost = edge[2];

            if (find(parents, start) != find(parents, end)) {
                union(parents, start, end);
                total += cost;
                lastCost = cost;
            }
        }

        System.out.println(total - lastCost);
    }

    public static int find(int[] parents, int a) {
        if (parents[a] != a) {
            parents[a] = find(parents, parents[a]);
        }
        return parents[a];
    }

    public static void union(int[] parents, int a, int b) {
        a = find(parents, a);
        b = find(parents, b);

        if (a < b) {
            parents[b] = a;
        } else {
            parents[a] = b;
        }
    }
}