/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 15900                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/15900                          #+#        #+#      #+#    */
/*   Solved: 2025/10/14 22:38:12 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main2 {
    static int N; // N 개의 정점 1부터 시작

    public static void main(String[] args) throws IOException {
        // 1.
        // 1에서 bfs로 visited에 각 노드까지의 거리 기록
        // Node를 담은 리스트를 돌면서 리프노드만 찾아서 visited 기록을 더해줌
        // 결과가 홀수면 승리 -> Yes 짝수면 -> No

        // 2.
        // 진입차수 정보를 담은 indegree를 만들어서 진입차수를 만들어줌

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        List<List<Integer>> graph = new ArrayList<>(N + 1);

        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }
        // visited
        int[] visited = new int[N + 1];

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        Queue<int[]> q = new ArrayDeque<>();

        // root node 1, cnt
        q.add(new int[] { 1, 0 });
        int result = 0;

        while (!q.isEmpty()) {
            int[] t = q.poll();
            int cur = t[0];
            int cnt = t[1];

            if (cur != 1 && graph.get(cur).size() == 1) {
                result += visited[cur];
            }

            for (int next : graph.get(cur)) {
                if (visited[next] == 0) {
                    visited[next] = cnt + 1;
                    q.add(new int[] { next, cnt + 1 });

                }
            }
        }

        // 짝수면 못이김 홀수면 이김 이길수 있으면 Yes
        String s = (result % 2 != 0) ? "Yes" : "No";
        System.out.println(s);
    }
}