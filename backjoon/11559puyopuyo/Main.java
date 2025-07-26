
import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int R = 12;
	static int C = 6;
	static char[][] graph;
	static int[][] visited;
	static int[] dr = {1, -1, 0, 0};
	static int[] dc = {0, 0, 1, -1};

	public static void main(String[] args) throws IOException {
		input();

		// while
		// boolean check -> if cant puyo then escape
		// int result -> if puyo ++
		// visited -> all time init used puyo dfs
		// 
		// do for r, for c and check can puyo dfs or bfs

		int cnt = 0;

		while (true) {
			boolean isBoom = chain();
			if (isBoom) {
				// move();
				moveToUseStack();
				cnt++;
			} else {
				break;
			}
		}

		System.out.println(cnt);
	}

	public static boolean chain() {
		visited = new int[R][C];
		int boomCnt = 0;

		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (visited[i][j] == 0 && graph[i][j] != '.') {
					boomCnt += bfs(graph[i][j], i, j);
				}
			}
		}

		if (boomCnt > 0) {
			return true;
		} else {
			return false;
		}
	}

	public static int bfs(char word, int r, int c) {
		int cnt = 1;
		visited[r][c] = 1;
		Queue<int[]> q = new LinkedList<>();
		List<int[]> boom = new ArrayList<>();
		q.add(new int[] {r, c});
		boom.add(new int[] {r, c});

		while (!q.isEmpty()) {
			int[] cur = q.poll();
			int curR = cur[0];
			int curC = cur[1];

			for (int d = 0; d < 4; d++) {
				int nR = curR + dr[d];
				int nC = curC + dc[d];

				if (nR < 0 || nR >= R || nC < 0 || nC >= C) {
					continue;
				}

				if (visited[nR][nC] == 0 && graph[nR][nC] == word) {
					q.add(new int[] {nR, nC});
					boom.add(new int[] {nR, nC});
					visited[nR][nC] = 1;
					cnt++;
				}
			}
		}

		if (cnt >= 4) {
			for (int[] b : boom) {
				int curR = b[0];
				int curC = b[1];

				graph[curR][curC] = '.';
			}
			return 1;
		}
		else {
			return 0;
		}
	}

	public static void moveToUseStack() {
		for (int c = 0; c < C; c++) {
			Stack<Character> stack = new Stack<>();
			for (int r = 0; r < R; r++) {
				if (graph[r][c] != '.') {
					stack.add(graph[r][c]);
				}
			}

			for (int r = R - 1; r >= 0; r--) {
				if (!stack.isEmpty()) {
					graph[r][c] = stack.pop();
				} else {
					graph[r][c] = '.';
				}
			}
		}
	}

	public static void move() {
		for (int c = 0; c < C; c++) {
			for (int r = R - 1; r > 0; r--) {
				if (graph[r][c] == '.') {
					int nR = r - 1;
					while (nR > 0 && graph[nR][c] == '.') {
						nR--;
					}
					if (graph[nR][c] != '.') {
						graph[r][c] = graph[nR][c];
						graph[nR][c] = '.';
					}
				}
			}
		}
	}

	public static void input() throws IOException {
		graph = new char[R][C];
		br = new BufferedReader(new InputStreamReader(System.in));

		for (int i = 0; i < R; i++) {
			graph[i] = br.readLine().toCharArray();
		}
	}
}
