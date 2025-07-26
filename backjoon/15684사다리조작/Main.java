
import java.util.*;
import java.io.*;

public class Main {
	static int N; // col
	static int M; // line cnt
	static int H; // row
	static int graph[][];
	static int visited[][];
	static int result;

	public static void main(String[] args) throws IOException {
		input();

		// for (int r = 0; r < H; r++) {
		// 	System.out.println(Arrays.toString(graph[r]));
		// }

		result = 4;
		dfs(0, 0, 0);
		if (result == 4) {
			result = -1;
		}
		System.out.println(result);
	}

	public static void dfs(int cnt, int curR, int curC) {
		if (cnt >= result) {
			return;
		}

		if (move()) {
			result = cnt;
			return;
		}

		for (int r = curR; r < H; r++) {
			for (int c = 0; c < N - 1; c++) {
				if (graph[r][c] == 0 && graph[r][c+1] == 0) {
					graph[r][c] = 1;
					graph[r][c+1] = -1;
					dfs(cnt + 1, r, c + 2);
					graph[r][c] = 0;
					graph[r][c+1] = 0;
				}
			}
		}

		return;
	}

	public static boolean move() {

		for (int c = 0; c < N; c++) {
			int startC = c;
			for (int r = 0; r < H; r++) {
				startC += graph[r][startC];
			}
			if (startC != c) {
				return false;
			}
		}
		return true;
	}

	public static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());

		graph = new int[H][N];
		visited = new int[H][N];

		for (int i = 0; i < M; i++) {
			int a, b;
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			// a -> row b -> col

			graph[a-1][b-1] = 1;
			graph[a-1][b] = -1;
		}
	}
}
