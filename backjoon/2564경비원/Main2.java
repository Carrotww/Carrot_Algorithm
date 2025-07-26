
import java.util.*;
import java.io.*;

public class Main {
	static int result;
	static int r;
	static int c;
	static BufferedReader br;
	static StringTokenizer st;
	static List<int[]> list;
	static int[][] visited;
	static int startR;
	static int startC;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		c = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		
		list = new ArrayList<>();

		for (int i = 0; i < n + 1; i++) {
			st = new StringTokenizer(br.readLine());
			int direct = Integer.parseInt(st.nextToken());
			int dist = Integer.parseInt(st.nextToken());
			int curR;
			int curC;

			if (direct == 1) {
				curR = 0;
				curC = dist;
			} else if (direct == 2) {
				curR = r;
				curC = dist;
			} else if (direct == 3) {
				curR = dist;
				curC = 0;
			} else {
				curR = dist;
				curC = c;
			}

			if (i != n) {
				list.add(new int[] {curR, curC});
			} else {
				startR = curR;
				startC = curC;
			}
		}
		bfs();

		for (int[] l : list) {
			result += visited[l[0]][l[1]];
		}

		System.out.println(result);
	}

	public static void bfs() {
		Queue<int[]> q = new LinkedList<>();
		visited = new int[r+1][c+1];
		for (int[] v : visited) {
			Arrays.fill(v, 10000);
		}
		visited[startR][startC] = 0;

		q.offer(new int[] {startR, startC});
		int[] dr = new int[] {1, -1, 0, 0};
		int[] dc = new int[] {0, 0, 1, -1};

		while (!q.isEmpty()) {
			int[] t = q.poll();
			int curR = t[0];
			int curC = t[1];

			for (int d = 0; d < 4; d++) {
				int nR = curR + dr[d];
				int nC = curC + dc[d];

				if (nR < 0 || nR > r || nC < 0 || nC > c) {
					continue;
				}

				if ((nR == 0 || nR == r || nC == 0 || nC == c) && visited[curR][curC] + 1 < visited[nR][nC]) {
					visited[nR][nC] = visited[curR][curC] + 1;
					q.add(new int[] {nR, nC});
				}
			}
		}
	}
}
