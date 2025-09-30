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
    static int[][] graph;
    static int[][] visited; // -1 init
    static Map<Integer, Integer> map;
    static Queue<Integer> q;
    static int cnt;
    static int N;
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new HashMap<>();
        graph = new int[100][100];
        q = new LinkedList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            map.put(a, b);
        }

        int value = 1;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                graph[i][j] = value;
                value++;
            }
        }

        for (int[] v : visited) {
            Arrays.fill(v, -1);
        }

        q.add(1);

        int cnt = 0;

        while (!q.isEmpty()) {
            cnt++;

            int cur = q.poll();

            if (cur == 100) {
                break;
            }

            boolean go = false;

            for (int i = 1; i <= 6; i++) {
                int next =  cur + i;
            }

            if (!go) {
                // 6번 가기
            }
        }

        System.out.println(cnt);
    }
}