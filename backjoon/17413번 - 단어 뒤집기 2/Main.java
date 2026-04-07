/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 17413                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/17413                          #+#        #+#      #+#    */
/*   Solved: 2026/03/21 18:02:13 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();

        StringBuilder sb = new StringBuilder();
        Stack<Character> s = new Stack<>();
        boolean istag = false;

        for (char c : line.toCharArray()) {
            // 일반 단어는 stack에 담고 공백이나 < 가 나오면 결과에 append
            // < 이면 > 가 나올때까지 그냥 결과에 담기
            if (c == '<' || c == '>' || c == ' ') {
                if (c == '<') {
                    istag = true;
                } else if (c == '>') {
                    istag = false;
                }
                flush(s, sb);
                sb.append(c);
                continue;
            }

            if (istag) {
                sb.append(c);
            } else {
                s.add(c);
            }
        }

        flush(s, sb);

        System.out.println(sb.toString());
    }

    private static void flush(Stack<Character> s, StringBuilder sb) {
        while (!s.empty()) {
            sb.append(s.pop());
        }
    }
}