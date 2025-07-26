
import java.io.*;
import java.util.*;

public class Main {
	static int T;
	static final int R = 5;
	static final int C = 9;
	static int[] dr = new int[] {1, -1, 0, 0};
	static int[] dc = new int[] {0, 0, 1, -1};
	static int total;
	static int totalMove;

	public static void main(String[] args) throws IOException {
		input();
	}

	public static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		T = Integer.parseInt(st.nextToken());

		for (int i = 0; i < T; i++) {
			total = 0;
			totalMove = 0;
			char[][] graph = new char[R][C];

			if (i > 0) br.readLine();

			for (int r = 0; r < R; r++) {
				String line = br.readLine();
				for (int c = 0; c < C; c++) {
					graph[r][c] = line.charAt(c);
					if (graph[r][c] == 'o') {
						total++;
					}
				}
			}

			solve(0, total, graph);

			System.out.println(total + " " + totalMove);
		}
	}

	public static boolean isInRange(int r, int c) {
		return r >= 0 && r < R && c >= 0 && c < C;
	}

	public static void solve(int move, int cnt, char graph[][]) {

		if (cnt < total) {
			total = cnt;
			totalMove = move;
		}

		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				if (graph[r][c] == 'o') {
					// if a pin can pass over another pin
					for (int d = 0; d < 4; d++) {
						int nR = r + dr[d];
						int nC = c + dc[d];

						int nnR = r + dr[d] * 2;
						int nnC = c + dc[d] * 2;

						if (isInRange(nR, nC) && graph[nR][nC] == 'o' && isInRange(nnR, nnC) && graph[nnR][nnC] == '.') {
							graph[nR][nC] = '.';
							graph[nnR][nnC] = 'o';
							graph[r][c] = '.';

							solve(move + 1, cnt - 1, graph);

							graph[nR][nC] = 'o';
							graph[nnR][nnC] = '.';
							graph[r][c] = 'o';
						}
					}
				}
			}
		}
	}
}
