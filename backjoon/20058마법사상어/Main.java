
import java.util.*;
import java.io.*;

class Fire {
	int r, c, m, s, d;

	public Fire(int r, int c, int m, int s, int d) {
		this.r = r;
		this.c = c;
		this.m = m;
		this.s = s;
		this.d = d;
	}
}

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int N;
	static int M;
	static int K; // 명령 횟수
	static Queue<Fire>[][][] graph;
	static int[] dr = new int[] {-1, -1, 0, 1, 1, 1, 0, -1};
	static int[] dc = new int[] {0, 1, 1, 1, 0, -1, -1, -1};

	public static void main(String[] args) throws IOException {
		// graph[r][c][2]
		// graph[r][c][0] = 움직이기 전
		// graph[r][c][1] = 움직인 후

		input();
		
		for (int i = 0; i < K; i++) {
			move();
			cal();
		}
		// 최종 계산

		int result = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				while (!graph[i][j][0].isEmpty()) {
					Fire cur = graph[i][j][0].poll();
					result += cur.m;
				}
			}
		}

		System.out.println(result);
	}

	public static void move() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				while (!graph[i][j][0].isEmpty()) {
					Fire cur = graph[i][j][0].poll();
					int nR = (cur.r + ((dr[cur.d] * cur.s) % N) + N) % N;
					int nC = (cur.c + ((dc[cur.d] * cur.s) % N) + N) % N;
					graph[nR][nC][1].add(new Fire(nR, nC, cur.m, cur.s, cur.d));
				}
			}
		}
	}

	public static void cal() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int nD = 1;
				int nM = 0;
				int nS = 0;
				int cnt = graph[i][j][1].size();
				if (cnt == 0) continue;
				if (cnt == 1) {
					graph[i][j][0].add(graph[i][j][1].poll());
					continue;
				}
				boolean odd = true;
				boolean even = true;

				while (!graph[i][j][1].isEmpty()) {
					Fire cur = graph[i][j][1].poll();
					nM += cur.m;
					nS += cur.s;
					if (cur.d % 2 == 0) {
						odd = false;
					} else {
						even = false;
					}
				}

				if (odd || even) {
					nD = 0;
				}
				nM /= 5;
				if (nM == 0) continue;

				nS /= cnt;

				for (int d = nD; d < 8; d+=2) {
					graph[i][j][0].add(new Fire(i, j, nM, nS, d));
				}
			}
		}
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		graph = new LinkedList[N][N][2];

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				graph[i][j][0] = new LinkedList<>();
				graph[i][j][1] = new LinkedList<>();
			}
		}

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int r = Integer.parseInt(st.nextToken());
			r--;
			int c = Integer.parseInt(st.nextToken());
			c--;
			int m = Integer.parseInt(st.nextToken());
			int s = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			graph[r][c][0].add(new Fire(r, c, m, s, d));
		}
	}
}
