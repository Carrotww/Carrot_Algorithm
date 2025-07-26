
import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int r;
	static int c;
	static int k;
	static int[][] graph;
	static int[][][] visited;
	static int[] dr = new int[] {1, -1, 0, 0};
	static int[] dc = new int[] {0, 0, 1, -1};
	static int result;

	public static void main(String[] args) throws IOException {
		input();

		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] {0, 0, 0});
		result = -1;

		while (!q.isEmpty()) {
			int[] t = q.poll();
			int curR = t[0];
			int curC = t[1];
			int curK = t[2];

			if (curR == r - 1 && curC == c - 1) {
				result = visited[curR][curC][curK];
				break;
			}

			for (int d = 0; d < 4; d++) {
				int nR = curR + dr[d];
				int nC = curC + dc[d];

				if (nR < 0 || nR >= r || nC < 0 || nC >= c) {
					continue;
				}

				if (graph[nR][nC] == 1 && curK < k && visited[nR][nC][curK+1] == 0) {
					visited[nR][nC][curK+1] = visited[curR][curC][curK] + 1;
					q.add(new int[] {nR, nC, curK + 1});
				} else if (graph[nR][nC] == 0 && visited[nR][nC][curK] == 0) {
					visited[nR][nC][curK] = visited[curR][curC][curK] + 1;
					q.add(new int[] {nR, nC, curK});
				}
			}
		}

		System.out.println(result);
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());

		graph = new int[r][c];
		visited = new int[r][c][k+1];
		visited[0][0][0] = 1;

		for (int i = 0; i < r; i++) {
			String t = br.readLine();
			for (int j = 0; j < c; j++) {
				graph[i][j] = t.charAt(j) - '0';
			}
		}
	}
}
