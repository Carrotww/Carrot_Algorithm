/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 17615                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/17615                          #+#        #+#      #+#    */
/*   Solved: 2025/07/28 09:08:16 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static char[] graph;
    public static void main(String[] args) throws IOException {
        input();

        System.out.println(Arrays.toString(graph));
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        System.out.println(N);
        String line = br.readLine();

        graph = new char[N];

        for (int i = 0; i < N; i++) {
            graph[i] = line.charAt(i);
        }
    }
}