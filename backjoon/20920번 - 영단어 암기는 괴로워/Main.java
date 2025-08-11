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

public class Main {
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

        List<String> words = new ArrayList<>(map.keySet());

        words.sort((a, b) -> {
            if (Integer.compare(map.get(a), map.get(b)) != 0) {
                return Integer.compare(map.get(b), map.get(a));
            } else if (a.length() != b.length()) {
                return b.length() - a.length();
            } else {
                return a.compareTo(b);
            }
        });

        StringBuilder sb = new StringBuilder();

        for (String word : words) {
            sb.append(word);
            sb.append("\n");
        }

        System.out.println(sb);

        // List<Map.Entry<String, Integer>> entryList = new ArrayList<>(map.entrySet());

        // entryList.sort((a, b) -> {
        //     if (a.getValue() != b.getValue()) {
        //         return Integer.compare(b.getValue(), a.getValue());
        //     }

        //     if (a.getKey().length() != b.getKey().length()) {
        //         return Integer.compare(b.getKey().length(), a.getKey().length());
        //     }

        //     return a.getKey().compareTo(b.getKey());
        // });

        // for (Map.Entry<String, Integer> entry : entryList) {
        //     System.out.println(entry.getKey());
        // }
    }
}