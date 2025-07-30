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

public class Main2 {
    static int N;
    static int M;
    static int H;
    static ArrayList<Integer>[] peopleAry;

    public static void main(String[] args) throws IOException {
        input();

        int[][] dp = new int[N][H+1];
        dp[0][0] = 1;
        for (int value : peopleAry[0]) {
            dp[0][value] = 1;
        }

        for (int people = 1; people < N; people++) {
            for (int height = 0; height <= H; height++) {
                dp[people][height] += dp[people-1][height];
                dp[people][height] %= 10007;

                for (int value : peopleAry[people]) {
                    if (value <= height) {
                        dp[people][height] += dp[people-1][height-value];
                        dp[people][height] %= 10007;
                    }
                }
            }
        }

        System.out.println(dp[N-1][H]);
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
        H = Integer.parseInt(st.nextToken());

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