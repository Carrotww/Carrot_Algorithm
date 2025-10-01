/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 16928                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/16928                          #+#        #+#      #+#    */
/*   Solved: 2025/09/30 23:11:22 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

// [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9,  10]
// [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

import java.util.*;
import java.io.*;

public class Main {
    static Map<Integer, Integer> map;
    static int[] visited;
    static int[] jump;
    static Queue<int[]> q;
    static int N;
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        q = new LinkedList<>();
        visited = new int[101];
        jump = new int[101];

        for (int i = 0; i < N + M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            jump[a] = b;
        }

        q.add(new int[] { 1, 0 });

        while (!q.isEmpty()) {

            int[] t = q.poll();
            int cur = t[0];
            int cnt = t[1];

            if (cur == 100) {
                break;
            }

            for (int i = 1; i <= 6; i++) {
                int next = cur + i;
                
                if (next > 100) continue;

                if (jump[next] != 0) {
                    next = jump[next];
                }

                if (visited[next] == 0) {
                    q.add(new int[] {next, cnt + 1});
                    visited[next] = cnt + 1;
                }
            }
        }

        System.out.println(visited[100]);
    }
}