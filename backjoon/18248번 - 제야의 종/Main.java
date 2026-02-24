/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 18248                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/18248                          #+#        #+#      #+#    */
/*   Solved: 2026/02/19 22:35:43 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        BitSet[] ary = new BitSet[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            BitSet bs = new BitSet();

            for (int j = 0; j < M; j++) {
                int value = Integer.parseInt(st.nextToken());

                if (value == 1) {
                    bs.set(j);
                }
            }
            ary[i] = bs;
        }

        boolean result = false;

        BitSet AllSet = new BitSet();
        for (int i = 0; i < M; i++) {
            AllSet.set(i);
        }

        for (int i = 0; i < N - 1; i++) {
            for (int j = i + 1; j < N; j++) {
                BitSet left = (BitSet) ary[i].clone();
                BitSet right = (BitSet) ary[j].clone();

                BitSet leftResult = (BitSet) ary[i].clone();

                // 왼쪽이 1 오른쪽이 0 인 것 찾기
                leftResult.andNot(right);

                // 왼쪽이 0 오른쪽이 1 인 것 찾기
                BitSet rightResult = (BitSet) AllSet.clone();
                rightResult.andNot(left);
                rightResult.and(right);

                if (!leftResult.isEmpty() && !rightResult.isEmpty()) {
                    result = true;
                }
            }
        }

        if (result) {
            System.out.println("NO");
        } else {
            System.out.println("YES");
        }
    }
}