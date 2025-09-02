/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2607                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2607                           #+#        #+#      #+#    */
/*   Solved: 2025/08/29 10:30:24 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

class Main {
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        int[][] wordAry = new int[N]['Z' - 'A' + 1];

        for (int i = 0; i < N; i++) {
            String word = br.readLine();
            for (int w = 0; w < word.length(); w++) {
                wordAry[i][word.charAt(w) - 'A']++;
            }
        }

        int result = 0;

        for (int i = 1; i < N; i++) {
            // start compare
            int beforeCnt = 0;
            int afterCnt = 0;

            for (int j = 0; j < 'Z' - 'A' + 1; j++) {
                wordAry[i][j] -= wordAry[0][j];

                if (wordAry[i][j] <= 0) {
                    beforeCnt += Math.abs(wordAry[i][j]);
                } else {
                    afterCnt += wordAry[i][j];
                }
            }

            if (beforeCnt > 1 || afterCnt > 1) {
                continue;
            }

            if (beforeCnt == 1 && afterCnt == 1) {
                result++;
            } else {
                result++;
            }
        }

        System.out.println(result);
    }
}
