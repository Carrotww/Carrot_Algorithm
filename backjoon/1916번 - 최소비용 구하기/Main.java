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

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());

        List<int[]>[] graph = new ArrayList[N + 1];
        int[] visited = new int[N + 1];
        Arrays.fill(visited, -1);

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

        visited[a] = 0;

        while (!pq.isEmpty()) {
            int[] node = pq.poll();

            int cnt = node[0];
            int cur = node[1];

            if (visited[cur] != cnt) continue;

            if (cur == b) {
                System.out.println(visited[b]);
                return;
            }

            // for 문으로 다음 갈 곳을 찾음
            // 다음 갈 곳이 -1 이거나 지금 cnt + 1 보다 작으면 감

            for (int[] nextNode : graph[cur]) {
                int next = nextNode[0];
                int nextCnt = nextNode[1];

                if (visited[next] == -1 || cnt + nextCnt < visited[next]) {
                    visited[next] = cnt + nextCnt;
                    pq.add(new int[] { cnt + nextCnt, next });
                }
            }
        }

        // 목적지 visited 를 출력함

        System.out.println(visited[b]);
    }
}