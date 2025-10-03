/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1063                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1063                           #+#        #+#      #+#    */
/*   Solved: 2025/10/03 17:38:59 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] king = new int[2];
        int[] rock = new int[2];

        String line = st.nextToken();
        king[0] = line.charAt(0) - 'A';
        king[1] = line.charAt(1) - '1';

        line = st.nextToken();
        rock[0] = line.charAt(0) - 'A';
        rock[1] = line.charAt(1) - '1';

        // 앞으로 움직일 횟수
        int N = Integer.parseInt(st.nextToken());

        // king = 1, rock = 2
        int[][] graph = new int[8][8];
        graph[king[0]][king[1]] = 1;
        graph[rock[0]][rock[1]] = 2;

        for (; N > 0; N--) {
            String direct = br.readLine().replace(" ", "");
            // 방향을 입력받고
            // 킹을 방향대로 움직인다
            // 킹이 나가는지 안나가는지 확인한다
            // 나가면 스킵
            // 도착 지점에 돌이 있다면 돌을 민다
            // 돌이 나간다면 취소한다
        }
    }
}