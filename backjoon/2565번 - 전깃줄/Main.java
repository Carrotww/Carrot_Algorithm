/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 2565                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/2565                           #+#        #+#      #+#    */
/*   Solved: 2026/04/06 21:43:34 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        List<int[]> ary = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            ary.add(new int[] {a, b});
        }

        ary.sort(Comparator.comparingInt(a -> a[0]));

        // ary [0] 기준으로 정렬이 되어 있으니 연속으로 증가하는 부분 순열 구하듯이 [1] 값을 기준으로 값을 구하자

        // int result = 1;

        // int[] dp = new int[N];

        // for (int i = 0; i < N; i++) {
        //     int end = ary.get(i)[1];
        //     dp[i] = 1;

        //     for (int j = 0; j < i; j++) {
        //         int start = ary.get(j)[1];

        //         if (start < end) {
        //             dp[i] = Math.max(dp[i], dp[j] + 1);
        //         }
        //     }

        //     result = Math.max(result, dp[i]);
        // }

        // binary search (left bound)
        int[] lis = new int[N];
        int len = 0;

        for (int i = 0; i < N; i++) {
            int target = ary.get(i)[1];
            int left = 0;
            int right = len;

            while (left < right) {
                int mid = (right - left) / 2 + left;

                if (lis[mid] < target) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }

            lis[left] = target;
            if (left == len) len++;
        }

        System.out.println(N - len);
    }
}
