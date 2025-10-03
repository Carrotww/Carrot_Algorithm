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
            boolean[][] beforeKilledEnemy = new boolean[N][M];
            for (int shooter : shooterAry) {
                // 가장 짧은 거리부터 계산함
                for (int d = 1; d <= D; d++) {
                    boolean isShoot = shootTime2(killedEnemy, beforeKilledEnemy, curR + 1, shooter, d);
                    if (isShoot)
                        break;
                }
            }
            // 이전에 쏜거는 killedEnemy에 기록한다

            for (int r = 0; r < N; r++) {
                for (int c = 0; c < M; c++) {
                    if (beforeKilledEnemy[r][c]) killedEnemy[r][c] = true;
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

    public static boolean shootTime2(boolean[][] killedEnemy, boolean[][] beforeKilledEnemy, int shooterR, int shooterC, int d) {
        // 왼쪽부터 죽이고 바로 오른쪽을 죽이면 안됨 가운데도 죽여야함
        // 왼쪽 coloum 범위를 구하고 그 때마다 row 계산을 해주면서 반복문을 하면 될 듯

        // 맨 왼쪽 = shooterC - d, 맨 오른쪽 = shooterC + d
        int startC = Math.max(shooterC - d, 0);
        int endC = Math.min(shooterC + d, M - 1);

        for (int c = startC; c <= endC; c++) {
            // row 범위를 구해줌
            int moveC = Math.abs(shooterC - c); // c 가 움직인 거리
            int can = d - moveC; // r이 움직일 수 있는 거리
            if (can <= 0) continue;

            int r = shooterR - can;
            if (r < 0 || r >= shooterR) continue;

            if (!killedEnemy[r][c] && graph[r][c] == 1) {
                beforeKilledEnemy[r][c] = true;
                return true;
            }
        }

        return false; 
    }

    // d 거리 만큼 왼쪽에서 찾아서 죽이면 바로 return
    public static boolean shootTime(boolean[][] killedEnemy, boolean[][] beforeKilledEnemy, int shooterR, int shooterC, int d) {
        // 궁수 위치 하나 윗 칸 shooter - 1 부터 -1 뺀 부분까지
        // d = 3 가정 shooterR = 4, enemy = 3 ~ 1 까지 그럼 범위는 shooterR - 1 ~ shooterR - d
        // d - shooterR - (현재 R) 가 coloum 갈 수 있는 거리
        for (int r = shooterR - 1; r >= shooterR - d; r--) {
            // 범위 넘을 수 있으니 체크
            if (r >= 0) {
                // col 의 범위는 d - (shooterR - r)
                // col 의 좌우 범위 = (d - (shotterR - r))
                // 좌우로 위 범위만큼 갈 수 있음
                int canShootRange = d - (shooterR - r);
                int startC = shooterC - canShootRange;
                int endC = shooterC + canShootRange;

                for (int c = startC; c <= endC; c++) {
                    if (c >= 0 && c < M && !killedEnemy[r][c] && graph[r][c] == 1) {
                        beforeKilledEnemy[r][c] = true;
                        return true;
                    }
                }
            }
        }
        return false;
    }
}