/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 20310                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/20310                          #+#        #+#      #+#    */
/*   Solved: 2025/08/29 10:30:48 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();

        int zeroCnt = 0;
        int oneCnt = 0;

        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == '0') {
                zeroCnt++;
            } else {
                oneCnt++;
            }
        }

        zeroCnt /= 2;
        oneCnt /= 2;

        StringBuilder sb = new StringBuilder();

        String line = input;

        for (int i = 0; i < line.length(); i++) {
            if (line.charAt(i) == '1' && oneCnt > 0) {
                oneCnt--;
                continue;
            }
            sb.append(line.charAt(i));
        }

        line = sb.toString();
        sb = new StringBuilder();

        for (int i = line.length() - 1; i >= 0; i--) {
            if (line.charAt(i) == '0' && zeroCnt > 0) {
                zeroCnt--;
                continue;
            }
            sb.append(line.charAt(i));
        }

        System.out.println(sb.reverse());
    }
}