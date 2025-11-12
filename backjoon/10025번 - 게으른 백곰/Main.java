/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 10025                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/10025                          #+#        #+#      #+#    */
/*   Solved: 2025/10/22 10:11:12 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] ary = new int[100001];

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int val = Integer.parseInt(st.nextToken());
            // ice
            int idx = Integer.parseInt(st.nextToken());

            ary[idx] = val;
        }

        int total = 0;
        int maxValue = 0;
        int resultIdx = -1;

        for (int i = 0; i < k * 2 + 1; i++) total += ary[i];

        for (int i = 1; i < ary.length - k * 2; i++) {
            total -= ary[i - 1];
            total += ary[i + k * 2];

            if (maxValue < total) {
                maxValue = total;
                resultIdx = i + k;
            }
        }

        System.out.println(maxValue);
    }
}