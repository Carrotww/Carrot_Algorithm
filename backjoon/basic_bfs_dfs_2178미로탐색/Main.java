
import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int[][] graph;
	static int[][] visited;
	static int R;
	static int C;
	static int dfsResult = Integer.MAX_VALUE;
	static int[] dr = new int[] {1, -1, 0, 0};
	static int[] dc = new int[] {0, 0, 1, -1};

	public static void main(String[] args) throws IOException {
		input();
		dfs(0, 0, 1);
		// bfs();

		System.out.println(dfsResult);
	}

	public static void dfs(int curR, int curC, int depth) {
		if (curR == R - 1 && curC == C - 1) {
			dfsResult = Math.min(dfsResult, depth);
			return;
		}

		visited[curR][curC] = 1;

		for (int d = 0; d < 4; d++) {
			int nR = curR + dr[d];
			int nC = curC + dc[d];

			if (nR < 0 || nR >= R || nC < 0 || nC >= C) {
				continue;
			}

			if (visited[nR][nC] == 0 && graph[nR][nC] == 1) {
				dfs(nR, nC, depth + 1);
				visited[nR][nC] = 0;
			}
		}
	}

	public static void bfs() {
		int[] dr = new int[] {1, -1, 0, 0};
		int[] dc = new int[] {0, 0, 1, -1};

		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] {0, 0});

		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				visited[i][j] = Integer.MAX_VALUE;
			}
		}
		visited[0][0] = 1;

		while (!q.isEmpty()) {
			int[] curNode = q.poll();
			int curR = curNode[0];
			int curC = curNode[1];

			if (curR == R - 1 && curC == C - 1) {
				break;
			}

			for (int d = 0; d < 4; d++) {
				int nR = curR + dr[d];
				int nC = curC + dc[d];

				if (nR >= R || nR < 0 || nC >= C || nC < 0) {
					continue;
				}

				if (visited[nR][nC] > visited[curR][curC] + 1 && graph[nR][nC] == 1) {
					visited[nR][nC] = visited[curR][curC] + 1;
					q.add(new int[] {nR, nC});
				}
			}
		}

		System.out.println(visited[R - 1][C - 1]);
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		graph = new int[R][C];
		visited = new int[R][C];

		for (int i = 0; i < R; i++) {
			String line = br.readLine();
			for (int j = 0; j < C; j++) {
				graph[i][j] = line.charAt(j) - '0';
			}
		}
	}
}
