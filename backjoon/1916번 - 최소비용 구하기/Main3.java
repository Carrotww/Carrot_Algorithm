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

public class Main3 {
    static int N;
    static int M;
    static List<int[]>[] graph;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N + 1];
        for (int i = 1; i < N + 1; i++)
            graph[i] = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph[a].add(new int[] { b, c });
        }

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        Queue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt((int[] a) -> a[0]));
        pq.add(new int[] { 0, start });

        visited = new int[N + 1];
        Arrays.fill(visited, -1);
        visited[start] = 0;

        while (!pq.isEmpty()) {
            int[] node = pq.poll();
            int cnt = node[0];
            int cur = node[1];

            // 도착한게 최소 값 쓰레기값이 나오면 없애줌
            if (visited[cur] != cnt)
                continue;

            // 정답 return
            if (cur == end) {
                System.out.println(cnt);
                return;
            }

            for (int[] nextNode : graph[cur]) {
                int next = nextNode[0];
                int nextCnt = nextNode[1];

                if (visited[next] == -1 || visited[next] > cnt + nextCnt) {
                    pq.add(new int[] { cnt + nextCnt, next });
                    visited[next] = cnt + nextCnt;
                }
            }
        }

        System.out.println(visited[end]);
    }
}