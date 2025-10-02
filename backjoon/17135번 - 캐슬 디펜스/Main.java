/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 17135                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/17135                          #+#        #+#      #+#    */
/*   Solved: 2025/10/02 22:03:47 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int M;
    static int D;
    static int[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());

        // 적 위치
        graph = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int val = Integer.parseInt(st.nextToken());
                graph[i][j] = val;
            }
        }

        // 정답 갱신해주기
        int result = 0;

        // 궁수 위치 모든 경우 다 돌리기
        for (int i = 0; i < M - 2; i++) {
            for (int j = i + 1; j < M - 1; j++) {
                for (int z = j + 1; z < M; z++) {
                    int val = solve(i, j, z);
                    result = Math.max(result, val);
                }
            }
        }

        System.out.println(result);
    }

    // graph 내리면서 활 쏘기
    // 굳이 graph를 변경할 필요는 없을 듯
    // 궁수가 올라가는 로직으로 하면 graph는 변경할 필요 없음
    public static int solve(int i, int j, int z) {
        int curR = N;
        int killCnt = 0;
        boolean[][] killedEnemy = new boolean[N][M];

        int[] shooterAry = new int[] { i, j, z };

        while (--curR >= 0) {
            // 궁수의 위치는 curR + 1 임
            // 현재 적의 위치는 curR

            // 궁수 3명 다 돌려서 killedEnemy 갱신하기
            for (int shooter : shooterAry) {
                // 가장 짧은 거리부터 계산함
                for (int d = 1; d <= D; d++) {
                    boolean isShoot = shootTime(killedEnemy, curR + 1, shooter, d);
                    if (isShoot)
                        break;
                }
            }
        }

        // killedEnemy 몇개인지 계산하고 return
        for (boolean[] e : killedEnemy) {
            for (int c = 0; c < M; c++) {
                if (e[c])
                    killCnt++;
            }
        }

        return killCnt;
    }

    // d 거리 만큼 왼쪽에서 찾아서 죽이면 바로 return
    public static boolean shootTime(boolean[][] killedEnemy, int shooterR, int shooterC, int d) {
        // 궁수 위치 하나 윗 칸 shooter - 1 부터 -1 뺀 부분까지
        for (int r = shooterR - 1; r < shooterR - d - 1; r--) {
            // 범위 넘을 수 있으니 체크
            if (r >= 0) {
                // col 의 범위는 d - (shooterR - r)
                // col 의 좌우 범위 = (d - (shotterR - r))
                // 좌우로 위 범위만큼 갈 수 있음
                int canShootRange = d - (shooterR - r);
                int startC = shooterC - canShootRange;
                int endC = shooterC + canShootRange;

                for (int c = startC; c <= endC; c++) {
                    if (c > 0 && c < M && graph[r][c] == 1) {
                        killedEnemy[r][c] = true;
                        return true;
                    }
                }
            }
        }
        return false;
    }
}