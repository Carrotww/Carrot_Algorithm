/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1325                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1325                           #+#        #+#      #+#    */
/*   Solved: 2026/03/01 22:36:37 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N, M;
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // union find 로는 안됨, union find는 한 노드가 한 부모만 가져야 함.
        // 이 문제에서는 여러 부모가 나올 수 있음
        // dfs

        List[] ary = new ArrayList[N + 1];

        for (int i = 0; i < N + 1; i++) {
            ary[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            ary[a].add(b);
            ary[b].add(a);
        }

        boolean[] visited = new boolean[N + 1];

        for (int i = 1; i < N + 1; i++) {
            if (visited[i]) continue;

            bfs();
        }
    }

    public static int bfs(int n, List[] ary, int start) {
        int cnt = 0;
        Deque<Integer> queue = new ArrayDeque<>();
        boolean[] visited = new boolean[n + 1];

        queue.add(start);
        
        while (!queue.isEmpty()) {
            int cur = queue.poll();
        }
        return 0;
    }
}
