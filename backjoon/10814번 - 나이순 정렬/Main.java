/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 10814                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/10814                          #+#        #+#      #+#    */
/*   Solved: 2025/09/24 23:10:54 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {

    static class Member {
        int age;
        String name;
        int cnt;

        Member(int a, String n, int c) {
            this.age = a;
            this.name = n;
            this.cnt = c;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        List<Member> ary = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int age = Integer.parseInt(st.nextToken());
            String name = st.nextToken();

            ary.add(new Member(age, name, i));
        }

        ary.sort(Comparator.comparingInt((Member m) -> m.age).thenComparingInt(m -> m.cnt));

        StringBuilder sb = new StringBuilder();

        for (Member m : ary) {
            sb.append(m.age);
            sb.append(" ");
            sb.append(m.name);
            sb.append("\n");
        }

        System.out.println(sb);
    }
}