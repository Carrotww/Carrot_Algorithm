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

public class Main {
    static int N; // col
    static int M; // row
    static int L; // net size
    static int K; // start cnt
    static ArrayList<int[]> starAry;
    public static void main(String[] args) throws IOException {
        input();

        int result = Integer.MAX_VALUE;

        for (int r = 0; r < M - L; r++) {
            for (int c = 0; c < N - L; c++) {
                int curCnt = K;

                for (int[] star : starAry) {
                    int starR = star[0];
                    int starC = star[1];

                    if ((starR >= r && starR <= r + L) && (starC >= c && starC <= c + L)) {
                        curCnt--;
                    }
                }

                result = Math.min(curCnt, result);
            }
        }

        System.out.println(result);
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

            starAry.add(new int[] {row, col});
        }
    }
}