/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 16235                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/16235                          #+#        #+#      #+#    */
/*   Solved: 2025/09/08 17:13:19 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main2 {
    static int N; // start r = 1, c = 1
    static int M;
    static int K;
    static ArrayList<Integer>[][] treeGraph;
    static int[][] foodGraph;
    static int[][] robotFoodGraph;

    public static void main(String[] args) throws IOException {
        input();

        for (int i = 0; i < K; i++) {
            // K years iter
            springAndSummer();
            fall();
            winter();
        }

        System.out.println(findTree());
    }

    static void springAndSummer() {
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                // 나무가 자신의 나이 만큼 양분을 먹음 어린 순서부터
                int food = foodGraph[r][c];
                // Collections.sort(treeGraph[r][c]);

                ArrayList<Integer> temp = new ArrayList<>();
                int leftFood = 0;

                // 정렬
                Collections.sort(treeGraph[r][c]);

                for (int treeAge : treeGraph[r][c]) {
                    if (food >= treeAge) {
                        food -= treeAge;
                        temp.add(treeAge + 1);
                        // summer
                    } else {
                        // 밥 못먹고 죽은 나무
                        leftFood += treeAge / 2;
                    }
                }

                treeGraph[r][c] = temp;
                foodGraph[r][c] = food + leftFood;
            }
        }
    }

    static void fall() {
        // 5 배수 나무 주위에 나이 1 짜리 나무를 만든다
        int[] dr = new int[] { -1, -1, -1, 0, 1, 1, 1, 0 };
        int[] dc = new int[] { -1, 0, 1, 1, 1, 0, -1, -1 };

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                for (int treeAge : treeGraph[r][c]) {
                    if (treeAge % 5 == 0) {
                        for (int d = 0; d < 8; d++) {
                            int nR = r + dr[d];
                            int nC = c + dc[d];

                            if (nR < 0 || nR >= N || nC < 0 || nC >= N) continue;

                            treeGraph[nR][nC].add(1);
                        }
                    }
                }
            }
        }
    }

    static void winter() {
        // 로봇이 땅에 양분 공급
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                foodGraph[r][c] += robotFoodGraph[r][c];
            }
        }
    }

    static int findTree() {
        // return result
        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                result += treeGraph[i][j].size();
            }
        }

        return result;
    }

    static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        treeGraph = new ArrayList[N][N];
        foodGraph = new int[N][N];
        robotFoodGraph = new int[N][N];

        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < N; c++) {
                treeGraph[r][c] = new ArrayList<>();
                foodGraph[r][c] = 5;
                robotFoodGraph[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            int age = Integer.parseInt(st.nextToken());
            treeGraph[r][c].add(age);
        }

        // init sort
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                Collections.sort(treeGraph[r][c]);
            }
        }
    }

    static void printGraph(int[][] g) {
        System.out.println("print graph");
        for (int[] a : g) {
            System.out.println(Arrays.toString(a));
        }
        System.out.println("end print graph");
    }
}