/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 20920                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/20920                          #+#        #+#      #+#    */
/*   Solved: 2025/08/06 17:36:31 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            if (line.length() >= M) {
                map.put(line, map.getOrDefault(line, 0) + 1);
            }
        }

        // 자주 나오는 단어일수록 앞에 배치한다.
        // 해당 단어의 길이가 길수록 앞에 배치한다.
        // 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

        List<String> ary = new ArrayList<>(map.keySet());
    }
}