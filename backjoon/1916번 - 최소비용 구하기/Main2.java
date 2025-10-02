/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1916                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1916                           #+#        #+#      #+#    */
/*   Solved: 2025/10/01 21:12:02 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        final int maxValue = Integer.MAX_VALUE;

        int N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());

        List<int[]>[] graph = new ArrayList[N + 1];
        int[] dist = new int [N + 1];
        boolean[] visited = new boolean[N + 1];
        Arrays.fill(dist, maxValue);

        for (int i = 1; i < N + 1; i++)
            graph[i] = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph[a].add(new int[] { b, c });
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(node -> node[0]));

        st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        pq.add(new int[] { 0, a });

        dist[a] = 0;

        while (!pq.isEmpty()) {
            int[] node = pq.poll();
            int cnt = node[0];
            int cur = node[1];

            // queue를 통과했는데 최소가 아니라면
            if (visited[cur]) continue;
            visited[cur] = true;

            if (cur == b) {
                System.out.println(dist[b]);
                return;
            }

            for (int[] nextNode : graph[cur]) {
                int next = nextNode[0];
                int nextCnt = nextNode[1];

                if (!visited[next] && dist[next] > nextCnt + cnt) {
                    dist[next] = nextCnt + cnt;
                    pq.add(new int[] {nextCnt + cnt, next});
                }
            }
        }

        System.out.println(dist[b]);
    }
}