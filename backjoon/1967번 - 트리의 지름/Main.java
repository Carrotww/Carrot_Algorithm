/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1967                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1967                           #+#        #+#      #+#    */
/*   Solved: 2025/10/15 17:45:52 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    static List<List<int[]>> graph;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>(N + 1);
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph.get(a).add(new int[] {b, c});
            graph.get(b).add(new int[] {a, c});
        }

        int fallNode = -1;
        int maxVal = bfs(1, N);
        for (int i = 1; i < N + 1; i++) {
            if (visited[i] == maxVal) { fallNode = i; break; }
        }

        System.out.println(bfs(fallNode, N));
    }

    static int bfs(int start, int nodeSize) {
        visited = new int[nodeSize + 1];
        Deque<int[]> dq = new ArrayDeque<>();

        dq.add(new int[] {start, 0});
        Arrays.fill(visited, -1);
        visited[start] = 0;

        while (!dq.isEmpty()) {
            int[] temp = dq.poll();
            int cur = temp[0];
            int cnt = temp[1];

            for (int[] next : graph.get(cur)) {
                int nextNode = next[0];
                int nextCnt = next[1];

                if (visited[nextNode] == -1 || visited[nextNode] > cnt + nextCnt) {
                    visited[nextNode] = cnt + nextCnt;
                    dq.add(new int[] {nextNode, cnt + nextCnt});
                }
            }
        }
        return Arrays.stream(visited).max().orElse(0);
    }
}