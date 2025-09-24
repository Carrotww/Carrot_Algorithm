/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1436                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1436                           #+#        #+#      #+#    */
/*   Solved: 2025/09/24 21:23:29 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        int num = 665;

        while (N > 0) {
            num++;
            if (check666(num)) {
                N--;
            }
        }

        System.out.println(num);
    }

    public static boolean check666(int num) {
        int cnt = 0;

        while (num > 0) {
            if (num % 10 == 6) {
                if (++cnt == 3) return true;
            } else {
                cnt = 0;
            }
            num /= 10;
        }

        return false;
    }
}