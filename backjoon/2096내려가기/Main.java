// https://www.acmicpc.net/problem/2096

import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int r;
	static int c = 3;
	static int[][] graph;
	static int[][] dpMax;
	static int[][] dpMin;

	public static void main(String[] args) throws IOException {
		input();
		dpMax = new int[r][c];
		dpMin = new int[r][c];
		// init
		dpMax[0] = graph[0];
		dpMin[0] = graph[0];

		int maxResult = 0;
		int minResult = 1000000;

		for (int i = 1; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (j == 0) {
					dpMax[i][j] = Math.max(graph[i][j] + dpMax[i-1][j], graph[i][j] + dpMax[i-1][j+1]);
					dpMin[i][j] = Math.min(graph[i][j] + dpMin[i-1][j], graph[i][j] + dpMin[i-1][j+1]);
				} else if (j == 1) {
					dpMax[i][j] = Math.max(Math.max(graph[i][j] + dpMax[i-1][j-1], graph[i][j] + dpMax[i-1][j]), graph[i][j] + dpMax[i-1][j+1]);
					dpMin[i][j] = Math.min(Math.min(graph[i][j] + dpMin[i-1][j-1], graph[i][j] + dpMin[i-1][j]), graph[i][j] + dpMin[i-1][j+1]);
				} else {
					dpMax[i][j] = Math.max(graph[i][j] + dpMax[i-1][j], graph[i][j] + dpMax[i-1][j-1]);
					dpMin[i][j] = Math.min(graph[i][j] + dpMin[i-1][j], graph[i][j] + dpMin[i-1][j-1]);
				}
			}
		}

		for (int i = 0; i < c; i++) {
			maxResult = Math.max(maxResult, dpMax[r-1][i]);
			minResult = Math.min(minResult, dpMin[r-1][i]);
		}

		System.out.println(maxResult + " " + minResult);
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		r = Integer.parseInt(st.nextToken());
		graph = new int[r][c];
		for (int i = 0; i < r; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 3; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
	}
}
