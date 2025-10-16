/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1167                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1167                           #+#        #+#      #+#    */
/*   Solved: 2025/10/16 23:35:44 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {
    static List<List<int[]>> graph;
    static int N;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 초기화
        N = Integer.parseInt(st.nextToken());
        graph = new ArrayList<>(N + 1);
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < N; i++) {
            // 입력
            st = new StringTokenizer(br.readLine());
            int cur = Integer.parseInt(st.nextToken());

            while (true) {
                int next = Integer.parseInt(st.nextToken());
                if (next == -1)
                    break;
                int cnt = Integer.parseInt(st.nextToken());

                graph.get(cur).add(new int[] { next, cnt });
            }
        }

        // 아무 노드에서 가장 먼 곳을 고르고 해당 노드에서 다시 먼 곳을 구하면 그게 지름
        int oneToFallNode = bfs(1);
        int result = bfs(oneToFallNode);
        System.out.println(visited[result]);
    }

    // bfs (start) 입력받고 가장 먼 노드 번호를 리턴함
    static int bfs(int start) {
        int result = -1;
        visited = new int[N + 1];
        Arrays.fill(visited, -1);
        visited[start] = 0;
        Deque<int[]> dq = new ArrayDeque<>();
        dq.add(new int[] { start, 0 });

        while (!dq.isEmpty()) {
            int[] temp = dq.pop();
            int cur = temp[0];
            int cnt = temp[1];

            for (int[] n : graph.get(cur)) {
                int next = n[0];
                int nCnt = n[1];

                if (visited[next] == -1 || visited[next] > cnt + nCnt) {
                    visited[next] = cnt + nCnt;
                    dq.add(new int[] { next, cnt + nCnt });
                }
            }
        }

        int maxCnt = 0;

        for (int i = 1; i < N + 1; i++) {
            if (maxCnt < visited[i]) {
                maxCnt = visited[i];
                result = i;
            }
        }
        return result;
    }
}
