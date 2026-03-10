/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 14889                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/14889                          #+#        #+#      #+#    */
/*   Solved: 2026/03/10 20:27:04 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {

    static int[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        graph = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int minScore = Integer.MAX_VALUE;
        Stack<Integer> s1 = new Stack<>();

        minScore = combination(s1, 0, N, minScore);

        System.out.println(minScore);

    }

    static int combination(Stack<Integer> s1, int index, int N, int minScore) {

        if (s1.size() == (N / 2)) {
            return Math.min(minScore, compareScore(s1, N));
        }

        for (int i = index; i < N; i++) {
            s1.add(i);
            minScore = Math.min(combination(s1, i + 1, N, minScore), minScore);
            s1.pop();
        }

        return minScore;
    }

    static int compareScore(Stack<Integer> s1, int N) {
        Set<Integer> set = new HashSet<>();
        List<Integer> ary1 = new ArrayList<>();
        List<Integer> ary2 = new ArrayList<>();

        for (int s : s1) {
            set.add(s);
            ary1.add(s);
        }

        for (int i = 0; i < N; i++) {
            if (!set.contains(i)) {
                ary2.add(i);
            }
        }

        int score1 = 0;
        int score2 = 0;

        for (int i = 0; i < N / 2; i++) {
            for (int j = 0; j < N / 2; j++) {
                score1 += graph[ary1.get(i)][ary1.get(j)];
                score2 += graph[ary2.get(i)][ary2.get(j)];
            }
        }

        return Math.abs(score1 - score2);
    }
}