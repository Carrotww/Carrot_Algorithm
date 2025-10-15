/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1967                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1967                           #+#        #+#      #+#    */
/*   Solved: 2025/10/15 17:45:52 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    static List<List<Integer>> graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>(N + 1);
        for (int i = 0; i < N - 1; i++) {
            
        }

        int result = 0;

        for (int i = 0; i < N + 1; i++) {
            result = Math.max(bfs(i, N), result);
        }
    }

    static int bfs(int start, int nodeSize) {
        int[] visited = new int[nodeSize + 1];

        return 0;
    }
}