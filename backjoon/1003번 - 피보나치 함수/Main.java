/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1003                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1003                           #+#        #+#      #+#    */
/*   Solved: 2025/11/12 16:07:42 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        int[] dp0 = new int[41];
        int[] dp1 = new int[41];

        dp0[0] = 1;
        dp1[0] = 0;

        dp0[1] = 0;
        dp1[1] = 1;

        for (int i = 2; i < 41; i++) {
            dp0[i] = dp0[i - 1] + dp0[i - 2];
            dp1[i] = dp1[i - 1] + dp1[i - 2];
        }
        
        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());

            System.out.println(dp0[N] + " " + dp1[N]);
        }
    }
}
