
import java.io.*;
import java.util.*;

public class Main4 {
	static int N, M, P;
	static int[] moveSize;
	static char[][] graph;
	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, 1, -1 };
	static Queue<int[]>[] qList;

	public static void main(String[] args) throws IOException {
		input();

		while (true) {
			boolean hasExpansion = false;

			for (int p = 0; p < P; p++) {
				Queue<int[]> q = qList[p];

				// 플레이어 p에 대해 moveSize[p]번 확장 수행
				for (int move = 0; move < moveSize[p] && !q.isEmpty(); move++) {
					int currentLevelSize = q.size();

					// 현재 거리의 모든 노드 처리
					for (int i = 0; i < currentLevelSize; i++) {
						int[] pos = q.poll();
						int r = pos[0];
						int c = pos[1];

						// 4방향 모두 확인
						for (int d = 0; d < 4; d++) {
							int nR = r + dr[d];
							int nC = c + dc[d];

							if (nR >= 0 && nR < N && nC >= 0 && nC < M && graph[nR][nC] == '.') {
								graph[nR][nC] = (char) (p + 1 + '0');
								q.add(new int[] { nR, nC });
								hasExpansion = true;
							}
						}
					}

					// 더 이상 확장할 셀이 없으면 조기 종료
					if (q.isEmpty())
						break;
				}
			}

			// 모든 플레이어가 더 이상 확장할 수 없으면 정지
			if (!hasExpansion)
				break;
		}

		// 영역 계산
		int[] result = new int[P];
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				char cc = graph[r][c];
				if (cc >= '1' && cc <= '9') {
					result[cc - '0' - 1]++;
				}
			}
		}

		StringBuilder sb = new StringBuilder();
		for (int count : result) {
			sb.append(count).append(" ");
		}
		System.out.println(sb.toString().trim());
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
				if (curC >= '1' && curC <= '9') {
					qList[curC - '0' - 1].add(new int[] { r, c });
				}
			}
		}
	}
}
