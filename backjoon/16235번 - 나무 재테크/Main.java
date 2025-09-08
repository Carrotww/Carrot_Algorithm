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

public class Main {
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
        }

        printGraph(foodGraph);

        System.out.println(findTree());
    }

    static int findTree() {
        // return result

        return 0;
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
            int age = Integer.parseInt(st.nextToken()) - 1;
            treeGraph[r][c].add(age);
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