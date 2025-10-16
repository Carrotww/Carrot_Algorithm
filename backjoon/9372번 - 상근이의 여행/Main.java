/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 9372                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/9372                           #+#        #+#      #+#    */
/*   Solved: 2025/10/14 22:29:32 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */


import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int result = 0;

            // a <-> b 왕복 비행기 m 번

            List<List<Integer>> graph = new ArrayList<>(N + 1);

            for (int j = 0; j < N + 1; j++) {
                graph.add(new ArrayList<>());
            }

            for (int m = 0; m < M; m++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                graph.get(a).add(b);
                graph.get(b).add(a);
            }

            int[] visited = new int[N + 1];

            result = bfs(graph, visited);

            sb.append(result);
            sb.append('\n');
        }

        System.out.println(sb);
    }

    static int bfs(List<List<Integer>> graph, int[] visited) {
        int result = 0;

        Queue<Integer> q = new ArrayDeque<>();
        q.add(1);
        visited[1] = 1;

        while (!q.isEmpty()) {
            int node = q.poll();
            for (int nextNode : graph.get(node)) {
                if (visited[nextNode] == 0) {
                    q.add(nextNode);
                    visited[nextNode] = 1;
                    result++;
                }
            }
        }

        return result;
    }
}
