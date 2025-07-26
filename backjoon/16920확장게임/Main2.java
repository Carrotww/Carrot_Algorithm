
import java.io.*;
import java.util.*;

public class Main2 {

	static int N; // row
	static int M; // col
	static int P; // player
	static int[] moveSize;
	static char[][] graph;
	static boolean[][] visited;
	static int[] dr = new int[] { -1, 1, 0, 0 };
	static int[] dc = new int[] { 0, 0, 1, -1 };
	static Queue<int[]>[] qList;

	public static void main(String[] args) throws IOException {
		input();

		// do each person bfs
		while (!isFull()) {
			for (int r = 0; r < N; r++) {
				for (int c = 0; c < M; c++) {
					char cc = graph[r][c];
					if (cc >= '1' && cc <= '9') {
						int pp = cc - '0';
						qList[pp - 1].add(new int[] { r, c, moveSize[pp - 1] });
					}
				}
			}

			for (int i = 0; i < P; i++) {
				Queue<int[]> curQ = qList[i];
				while (!curQ.isEmpty()) {
					int[] curList = curQ.poll();
					int curR = curList[0];
					int curC = curList[1];
					int curCnt = curList[2];

					for (int d = 0; d < 4; d++) {
						int nR = curR + dr[d];
						int nC = curC + dc[d];

						if (nR < 0 || nR >= N || nC < 0 || nC >= M)
							continue;

						// if curCnt > 1 and graph value is '.'
						if (graph[nR][nC] == '.' && curCnt > 0) {
							graph[nR][nC] = (char) ((i + 1) + '0');
							curQ.add(new int[] { nR, nC, curCnt - 1 });
						}
					}
				}
			}
		}

		// for (int r = 0; r < N; r++) {
		// System.out.println(Arrays.toString(graph[r]));
		// }

		StringBuilder sb = new StringBuilder();
		int[] result = new int[P];
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				char cc = graph[r][c];
				if (cc >= '1' && cc <= '9') {
					int pp = cc - '0';
					result[pp - 1]++;
				}
			}
		}

		for (int r : result) {
			sb.append(r);
			sb.append(" ");
		}

		System.out.println(sb);

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
		qList = new Queue[P];

		for (int i = 0; i < P; i++) {
			qList[i] = new ArrayDeque<>();
		}

		for (int r = 0; r < N; r++) {
			String line = br.readLine();
			for (int c = 0; c < M; c++) {
				char curC = line.charAt(c);
				graph[r][c] = curC;
			}
		}
	}
}
