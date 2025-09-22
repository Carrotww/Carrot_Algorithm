/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 20061                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/20061                          #+#        #+#      #+#    */
/*   Solved: 2025/09/11 23:06:17 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {
    // x = row, y = col
    // t = 1 -> (x, y)
    // t = 2 -> (x, y), (x, y + 1)
    // t = 3 -> (x, y), (x + 1, y)

    static ArrayList<ArrayList<int[]>> blockArray = new ArrayList<>();
    static boolean[][] graph = new boolean[10][10];
    static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            ArrayList<int[]> block = new ArrayList<>();
            block.add(new int[] {r, c});

            if (t == 2) {
                block.add(new int[] {r, c + 1});
            } else if (t == 3) {
                block.add(new int[] {r + 1, c});
            }

            blockArray.add(block);
        }

        // 블럭 돎면서 하나하나 처리하기

        for (ArrayList<int[]> block : blockArray) {
            // 파란색으로 움직이기
            moveBlue(block);
            moveGreen(block);

            // 터뜨리기, 터졌으면 움직이기 터지면 점수
            popBlue();
            popGreen();

            // 경계 확인해서 밀어주기
            checkBlueLine();
            checkGreenLine();
        }

        for (boolean[] g : graph) {
            System.out.println(Arrays.toString(g));
        }

        System.out.println(result);
    }

    static void moveBlue(ArrayList<int[]> block) {

        ArrayList<int[]> curBlock = block;

        // 오른쪽으로 움직이기 col ++
        while (true) {
            boolean canMove = true;
            // block 둘 다 하나씩 밀어ㅇ서 자리 있으면
            for (int[] b : curBlock) {
                int r = b[0];
                int c = b[1];

                // 범위 확인 하고 자리 있는지 확인
                if (c < 10 && graph[r][c + 1]) {
                    continue;
                } else {
                    canMove = false;
                    break;
                }
            }

            // 움직이기
            if (canMove) {
                for (int[] b : curBlock) {
                    b[1] ++;
                }
            } else {
                // 없으면 종료
                break;
            }
        }

        for (int[] b : curBlock) {
            graph[b[0]][b[1]] = true;
        }
    }

    static void moveGreen(ArrayList<int[]> block) {
        ArrayList<int[]> curBlock = block;

        // 아래로 움직이기 row ++
        while (true) {
            boolean canMove = true;
            // block 둘 다 하나씩 밀어ㅇ서 자리 있으면
            for (int[] b : curBlock) {
                int r = b[0];
                int c = b[1];

                // 범위 확인 하고 자리 있는지 확인
                if (r < 10 && graph[r + 1][c]) {
                    continue;
                } else {
                    canMove = false;
                    break;
                }
            }

            // 움직이기
            if (canMove) {
                for (int[] b : curBlock) {
                    b[0] ++;
                }
            } else {
                // 없으면 종료
                break;
            }
        }

        for (int[] b : curBlock) {
            graph[b[0]][b[1]] = true;
        }
    }

    static void popBlue() {
        for (int c = 6; c < 10; c++) {
            boolean canMove = true;

            for (int r = 0; r < 4; r++) {
                if (!graph[r][c]) {
                    canMove = false;
                    break;
                }
            }

            if (canMove) {
                // 터뜨리기
                // 터지면 아래칸으로 밀고 다시 확인해야 한다.
                for (int r = 0; r < 4; r++) {
                    graph[r][c] = false;
                }

                // 움직여 주기
                for (int cc = c; cc > 5; cc--) {
                    for (int rr = 0; rr < 4; rr++) {
                        graph[rr][cc] = graph[rr][cc-1];
                        graph[rr][cc-1] = false;
                    }
                }

                result++;
            }
        }
    }

    static void popGreen() {

        for (int r = 6; r < 10; r++) {
            boolean canMove = true;

            for (int c = 0; c < 4; c++) {
                if (!graph[r][c]) {
                    canMove = false;
                    break;
                }
            }

            if (canMove) {
                for (int c = 0; c < 4; c++) {
                    graph[r][c] = false;
                }

                for (int rr = r; rr > 5; rr--) {
                    for (int cc = 0; cc < 4; cc++) {
                        graph[rr][cc] = graph[rr-1][cc];
                        graph[rr-1][cc] = false;
                    }
                }

                result++;
            }
        }
    }

    static void checkBlueLine() {
        // 파란 경계 확인해서 오른쪽으로 밀기
        int moveCnt = 0;

        for (int c = 4; c < 5; c++) {
            for (int r = 0; r < 4; r++) {
                if (graph[r][c]) {
                    moveCnt++;
                    break;
                }
            }
        }

        for (int i = 0; i < moveCnt; i++) {
            // 경계에 있는 만큼 밀어줘야 한다.
            for (int c = 9; c > 4; c--) {
                for (int r = 0; r < 4; r++) {
                    graph[r][c] = graph[r][c-1];
                }
            }
        }
    }

    static void checkGreenLine() {
        int moveCnt = 0;

        for (int r = 4; r < 5; r++) {
            for (int c = 0; c < 4; c++) {
                if (graph[r][c]) {
                    moveCnt++;
                    break;
                }
            }
        }

        for (int i = 0; i < moveCnt; i++) {
            for (int c = 9; c > 4; c--) {
                for (int r = 0; r < 4; r++) {
                    graph[r][c] = graph[r-1][c];
                }
            }
        }
    }
}