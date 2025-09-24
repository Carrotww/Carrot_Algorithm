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

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        int num = 665;

        while (N > 0) {
            if (check666(num)) {
                N--;
            }
            num++;
        }

        System.out.println(num-1);
    }

    public static boolean check666(int num) {
        boolean result = false;

        String s = Integer.toString(num);

        int cnt = 0;
        int size = s.length();

        for (int i = 0; i < size; i++) {
            if (s.charAt(i) == '6') {
                cnt++;
                if (cnt >= 3) {
                    return true;
                }
            } else {
                cnt = 0;
            }
        }

        return result;
    }
}