
import java.io.*;
import java.util.*;

public class Main {

	static int N; // row
	static int M; // col
	static int P; // player
	static int[] moveSize;
	static char[][] graph;
	static int[] dr = new int[] { -1, 1, 0, 0 };
	static int[] dc = new int[] { 0, 0, 1, -1 };

	public static void main(String[] args) throws IOException {
		input();

		while (!isFull()) {
			for (int p = 1; p < P + 1; p++) {
				move(p);
			}
		}

		for (int r = 0; r < N; r++) {
			Arrays.toString(graph[r]);
		}

		StringBuilder sb = new StringBuilder();
		int[] result = new int[P];

		for (int p = 1; p < P + 1; p++) {
			for (int r = 0; r < N; r++) {
				for (int c = 0; c < M; c++) {
					if (graph[r][c] == ((char) +p) + '0') {
						result[p - 1]++;
					}
				}
			}
		}

		for (int i = 0; i < P; i++) {
			sb.append(result[i] + " ");
		}

		System.out.println(sb);
	}

	public static void move(int curP) {
		boolean[][] visited = new boolean[N][M];

		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				if (graph[r][c] != (char) (curP + '0')) {
					visited[r][c] = true;
				}
			}
		}

		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				if (!visited[r][c] && graph[r][c] == ((char) curP) + '0') {
					goP(visited, curP, r, c);
				}
			}
		}

		return;
	}

	public static void goP(boolean[][] visited, int curP, int curR, int curC) {
		int pMove = moveSize[curP - 1];

		for (int d = 0; d < 4; d++) {
			for (int i = 1; i < pMove + 1; i++) {
				int nR = dr[d] * i + curR;
				int nC = dc[d] * i + curC;

				if (nR < 0 || nR >= N || nC < 0 || nC >= M)
					continue;
				if (graph[nR][nC] == '.') {
					graph[nR][nC] = (char) (curP + '0');
				}
			}
		}

		return;
	}

	public static boolean isFull() {
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				if (graph[r][c] == '.') {
					return false;
				}
			}
		}

		return true;
	}

	public static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		P = Integer.parseInt(st.nextToken());

		moveSize = new int[P];
		st = new StringTokenizer(br.readLine());

		for (int i = 0; i < P; i++) {
			moveSize[i] = Integer.parseInt(st.nextToken());
		}

		graph = new char[N][M];
		for (int r = 0; r < N; r++) {
			String line = br.readLine();
			for (int c = 0; c < M; c++) {
				graph[r][c] = line.charAt(c);
			}
		}
	}
}
