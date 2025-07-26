
import java.io.*;
import java.util.*;

public class Main3 {

	static int N; // row
	static int M; // col
	static int P; // player
	static int[] moveSize;
	static char[][] graph;
	static boolean[][] visited;
	static int[] dr = new int[] { -1, 1, 0, 0 };
	static int[] dc = new int[] { 0, 0, 1, -1 };
	static Queue<int[]>[] qList;
	static int cnt = 1;

	public static void main(String[] args) throws IOException {
		input();

		// printGraph();
		while (true) {
			boolean isFull = true;

			for (int p = 0; p < P; p++) {
				int lotate = moveSize[p];
				Queue<int[]> q = qList[p];

				for (int i = 0; i < lotate && !q.isEmpty(); i++) {
					int qSize = q.size();

					for (int s = 0; s < qSize; s++) {
						int[] list = q.poll();
						int r = list[0];
						int c = list[1];

						for (int d = 0; d < 4; d++) {
							int nR = r + dr[d];
							int nC = c + dc[d];

							if (nR < 0 || nR >= N || nC < 0 || nC >= M)
								continue;

							if (graph[nR][nC] == '.') {
								graph[nR][nC] = (char) (p + 1 + '0');
								q.add(new int[] { nR, nC });
								isFull = false;
							}
						}
					}
					// printGraph();
				}
			}

			if (isFull) {
				break;
			}
		}

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

	public static void printGraph() {
		System.out.println("---------------" + cnt + "------------------");
		for (int r = 0; r < N; r++) {
			System.out.println(Arrays.toString(graph[r]));
		}
		System.out.println("-------------------------------------------");
		cnt++;
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
				if (curC >= '0' && curC <= '9') {
					int cNum = curC - '0';
					graph[r][c] = curC;
					qList[cNum - 1].add(new int[] { r, c });
				} else {
					graph[r][c] = curC;
				}
			}
		}
	}
}
