/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 18427                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/18427                          #+#        #+#      #+#    */
/*   Solved: 2025/07/29 20:21:03 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;

import java.io.*;

public class Main {
    static int N;
    static int M;
    static int H;
    static ArrayList<Integer>[] peopleAry;

    public static void main(String[] args) throws IOException {
        input();

        int[][] dp = new int[N+1][M+1];

        // init
        dp[0][0] = 1;

        for (int i = 1; i <= N; i++) {
            for (int j = 0; j <= M; j++) {
                dp[i][j] += dp[i-1][j];
                for (int value : peopleAry[i-1]) {
                    if (value <= j) {
                        dp[i][j] += dp[i-1][j-value];
                    }
                }
            }
        }

        System.out.println(dp[N][M]);
    }

    public static void print() {
        for (ArrayList<Integer> ary : peopleAry) {
            System.out.println(ary);
        }
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        peopleAry = new ArrayList[N];

        for (int i = 0; i < N; i++) {
            peopleAry[i] = new ArrayList<>();
            String line = br.readLine();
            String[] nums = line.split(" ");
            for (String num : nums) {
                peopleAry[i].add(Integer.parseInt(num));
            }
            // backjoon cant compile java-17
            // peopleAry[i] = new ArrayList<>(
            // Arrays.stream(line.split(" "))
            //     .map(Integer::parseInt)
            //     .toList()
            // );
        }
    }
}