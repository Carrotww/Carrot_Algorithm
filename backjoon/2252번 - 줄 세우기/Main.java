/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2252                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2252                           #+#        #+#      #+#    */
/*   Solved: 2026/03/03 23:03:45 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N, M;
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // topology sort
        int[] indegree = new int[N + 1];
        List<Integer>[] ary = new ArrayList[N + 1];
        Queue<Integer> q = new ArrayDeque<>();

        for (int i = 0; i < N + 1; i++) ary[i] = new ArrayList<>();

        int a, b;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            // b가 더 크다
            indegree[b]++;
            ary[a].add(b);
        }

        for (int i = 1; i < N + 1; i++) {
            if (indegree[i] == 0) {
                q.add(i);
            }
        }

        StringBuilder sb = new StringBuilder();
        while (!q.isEmpty()) {
            int cur = q.poll();

            for (int next : ary[cur]) {
                indegree[next]--;
                if (indegree[next] == 0) {
                    q.add(next);
                }
            }

            sb.append(cur);
            sb.append(" ");
        }

        System.out.println(sb.toString());
    }
}