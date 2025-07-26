import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int r;
	static int c = 3;
	static int[][] graph;
	static int[][][] dp;

	public static void main(String[] args) throws IOException {
		input();
		dp = new int[r][c][2];
		// init
		for (int i = 0; i < 3; i++) {
			dp[0][i][0] = graph[0][i];
			dp[0][i][1] = graph[0][i];
		}

		for (int i = 1; i < r; i++) {
			for (int j = 0; j < c; j++) {
				if (j == 0) {
					dp[i][j][0] = Math.max(graph[i][j] + dp[i-1][j][0], graph[i][j] + dp[i-1][j+1][0]);
					dp[i][j][1] = Math.min(graph[i][j] + dp[i-1][j][1], graph[i][j] + dp[i-1][j+1][1]);
				} else if (j == 1) {
					dp[i][j][0] = Math.max(Math.max(graph[i][j] + dp[i-1][j-1][0], graph[i][j] + dp[i-1][j][0]), graph[i][j] + dp[i-1][j+1][0]);
					dp[i][j][1] = Math.min(Math.min(graph[i][j] + dp[i-1][j-1][1], graph[i][j] + dp[i-1][j][1]), graph[i][j] + dp[i-1][j+1][1]);
				} else {
					dp[i][j][0] = Math.max(graph[i][j] + dp[i-1][j][0], graph[i][j] + dp[i-1][j-1][0]);
					dp[i][j][1] = Math.min(graph[i][j] + dp[i-1][j][1], graph[i][j] + dp[i-1][j-1][1]);
				}
			}
		}

		int maxResult = Integer.MIN_VALUE;
		int minResult = Integer.MAX_VALUE;

		for (int i = 0; i < c; i++) {
			maxResult = Math.max(maxResult, dp[r-1][i][0]);
			minResult = Math.min(minResult, dp[r-1][i][1]);
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
