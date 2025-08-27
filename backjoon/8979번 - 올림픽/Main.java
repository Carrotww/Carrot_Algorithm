/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 8979                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/8979                           #+#        #+#      #+#    */
/*   Solved: 2025/08/26 22:29:25 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int target;
    static ArrayList<Integer>[] ary;

    public static void main(String[] args) throws IOException {
        input();

        Arrays.sort(ary, (a, b) -> {
            if (a.get(1) != b.get(1))
                return b.get(1) - a.get(1);
            else if (a.get(2) != b.get(2))
                return b.get(2) - a.get(2);
            return b.get(3) - a.get(3);
        });

        int rank = 1;
        int prevRank = 1;

        ArrayList<Integer> prev = ary[0];

        if (prev.get(0) == target) {
            System.out.println(1);
            return;
        }

        for (int i = 1; i < N; i++) {
            boolean isSame = true;
            rank++;

            for (int j = 0; j < 3; j++) {
                if (prev.get(j + 1) != ary[i].get(j + 1)) {
                    isSame = false;
                    break;
                }
            }

            if (!isSame) {
                prev = ary[i];
                prevRank = rank;
            }

            if (ary[i].get(0) == target) {
                System.out.println(prevRank);
                break;
            }
        }

    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        target = Integer.parseInt(st.nextToken());

        ary = new ArrayList[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            ArrayList<Integer> a = new ArrayList<>();

            while (st.hasMoreTokens()) {
                a.add(Integer.parseInt(st.nextToken()));
            }

            ary[i] = a;
        }
    }
}