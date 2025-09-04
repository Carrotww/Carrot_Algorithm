/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 14658                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/14658                          #+#        #+#      #+#    */
/*   Solved: 2025/09/02 16:11:35 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main2 {
    static int N; // col
    static int M; // row
    static int L; // net size
    static int K; // start cnt

    static ArrayList<int[]> starAry;

    public static void main(String[] args) throws IOException {
        input();

        int result = 0;

        for (int[] star1 : starAry) {
            for (int[] star2 : starAry) {
                int cnt = 0;
                for (int[] targetStar : starAry) {
                    int curR = targetStar[0];
                    int curC = targetStar[1];

                    if (curR >= star1[0] && curR <= star1[0] + L && curC >= star2[1] && curC <= star2[1] + L) {
                        cnt++;
                    }
                }

                result = Math.max(result, cnt);
            }
        }

        System.out.println(K - result);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        starAry = new ArrayList<>();

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int col = Integer.parseInt(st.nextToken());
            int row = Integer.parseInt(st.nextToken());

            starAry.add(new int[] { row, col });
        }
    }
}