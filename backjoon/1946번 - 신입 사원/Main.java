/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1946                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1946                           #+#        #+#      #+#    */
/*   Solved: 2026/03/04 22:28:07 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {
    public static void main2(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());
        int N;
        StringBuilder sb = new StringBuilder();

        while (T-- > 0) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            // init 1차 시험 순위대로
            int[] ary = new int[N + 1];
            int a, b;

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                a = Integer.parseInt(st.nextToken());
                b = Integer.parseInt(st.nextToken());

                ary[a] = b;
            }

            // 1등의 서류 등수
            int score = ary[1];
            // 1등은 합격
            int cnt = 1;

            for (int i = 2; i < N + 1; i++) {
                // 앞 사람보다 면점 등수 높아야 합격
                if (score >= ary[i]) cnt++;
                // 제일 잘 본 면접 등수로
                score = Math.min(score, ary[i]);
            }

            sb.append(cnt);
            if (T == 0) continue;
            sb.append('\n');
        }

        System.out.println(sb.toString());
    }

    // 입력 받고 정렬
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());
        int N;
        int a, b;
        StringBuilder sb = new StringBuilder();

        while (T-- > 0) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            List<int[]> ary = new ArrayList<>();
            
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                a = Integer.parseInt(st.nextToken());
                b = Integer.parseInt(st.nextToken());
                ary.add(new int[] {a, b});
            }

            Collections.sort(ary, Comparator.comparingInt(x -> x[0]));

            int score = ary.get(0)[1];
            int cnt = N;

            for (int i = 1; i < N; i++) {
                // compare rank
                if (score < ary.get(i)[1]) cnt--;

                // renew score min rank
                score = Math.min(score, ary.get(i)[1]);
            }

            sb.append(cnt);
            sb.append('\n');
        }
        
        System.out.println(sb.toString());
    }
}

