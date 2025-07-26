/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 18405                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/18405                          #+#        #+#      #+#    */
/*   Solved: 2025/07/25 15:09:00 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int K;
	static int[][] graph;
	static Queue<int[]> q;
	static int[] dr = new int[] { 1, -1, 0, 0 };
	static int[] dc = new int[] { 0, 0, 1, -1 };
	static int targetR;
	static int targetC;
	static int time;

	public static void main(String[] args) throws IOException {
		input();

		// for (int[] g : graph) {
		// System.out.println(Arrays.toString(g));
		// }

		for (int t = 0; t < time; t++) {
			int size = q.size();
			for (int i = 0; i < size; i++) {
				int[] cur = q.poll();
				int curR = cur[0];
				int curC = cur[1];
				int curV = cur[2];

				for (int d = 0; d < 4; d++) {
					int nR, nC;
					nR = curR + dr[d];
					nC = curC + dc[d];

					if (nR < 0 || nR >= N || nC < 0 || nC >= N) {
						continue;
					}

					if (graph[nR][nC] == 0) {
						graph[nR][nC] = curV;
						q.add(new int[] { nR, nC, curV });
					}
				}
			}
		}
		System.out.println(graph[targetR][targetC]);
	}

	public static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		graph = new int[N][N];
		q = new LinkedList<>();

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		st = new StringTokenizer(br.readLine());

		time = Integer.parseInt(st.nextToken());
		targetR = Integer.parseInt(st.nextToken()) - 1;
		targetC = Integer.parseInt(st.nextToken()) - 1;

		for (int i = 1; i <= K; i++) {
			for (int r = 0; r < N; r++) {
				for (int c = 0; c < N; c++) {
					if (graph[r][c] == i) {
						q.add(new int[] { r, c, i });
					}
				}
			}
		}
	}
}
