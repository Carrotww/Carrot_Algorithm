/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1516                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1516                           #+#        #+#      #+#    */
/*   Solved: 2026/03/06 19:13:22 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        // 위상 정렬 먼저 하기
        // 진입차수
        int[] indegree = new int[N + 1];
        // graph
        List<Integer>[] ary = new ArrayList[N + 1];
        // default
        int[] selfTime = new int[N + 1];

        Queue<Integer> q = new ArrayDeque<>();

        for (int i = 0; i < N + 1; i++) ary[i] = new ArrayList<>();

        for (int i = 1; i < N + 1; i++) {
            st = new StringTokenizer(br.readLine());

            int time = Integer.parseInt(st.nextToken());
            selfTime[i] = time;

            while (true) {
                int next = Integer.parseInt(st.nextToken());

                if (next == -1) break;

                indegree[i]++;
                // next 가 먼저 지어야 하는 건물
                ary[next].add(i);
            }
        }

        // topology sort
        // init
        for (int i = 1; i < N + 1; i++) {
            if (indegree[i] == 0) q.add(i);
        }

        // 다음 건물을 지어야 할 때 visited에 add 해주고
        // 다음 건물이 pop 되었을 때 처리 해주자
        // 가장 큰 값으로

        List<Integer>[] visited = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) visited[i] = new ArrayList<>();
        int[] dp = new int[N + 1];

        while (!q.isEmpty()) {
            // 0인 것 뽑기
            int cur = q.poll();
            int curTime = selfTime[cur];
            int max = 0;

            if (!visited[cur].isEmpty()) {
                for (int v : visited[cur]) max = Math.max(max, v);
                curTime += max;
            }

            for (int next : ary[cur]) {
                indegree[next]--;
                visited[next].add(curTime);
                if (indegree[next] == 0) {
                    q.add(next);
                }
            }

            dp[cur] = curTime;
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 1; i < N + 1; i++) {
            sb.append(dp[i]);
            if (i == N) continue;
            sb.append('\n');
        }

        System.out.println(sb.toString());
    }
}
