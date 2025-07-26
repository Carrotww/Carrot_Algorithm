import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int r;
	static int c;
	static int result;
	static int[][] graph;
	static int[][] visited;
	static List<int[]> shark;

	public static void main(String[] args) throws IOException {
		input();

		// 1. 1의 칸이 상어가 있는 칸
		// 2. bfs로 상어가 있는 자리에서 시작해서 visited(안전거리) 를 갱신해준다
		// 3. visited의 초기값은 최대값으로 설정하고 상어가 최단거리로 갈 수 있다면 갱신해준다.
		// 4. 대각선으로 갈 수 있는것을 잊지 말자

		// visited 초기화 1 <= r, c <= 50
		visited = new int[r][c];
		for (int i = 0; i < r; i++) {
			Arrays.fill(visited[i], 2500);
		}

		for (int[] s : shark) {
			visited[s[0]][s[1]] = 0;
			bfs(s);
		}

		// 최대값 출력
		result = 0;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				result = Math.max(result, visited[i][j]);
			}
		}
		System.out.println(result);
	}

	public static void bfs(int[] xy) {
		// write int[] dr, dc and that can move diagonally
		// need to update visited while moving

		// write from the upper left diagonal
		int[] dr = new int[] {-1, -1, -1, 0, 1, 1, 1, 0};
		int[] dc = new int[] {-1, 0, 1, 1, 1, 0, -1, -1};
		Queue<int[]> q = new LinkedList<>();
		q.offer(xy);

		while (!q.isEmpty()) {
			int[] a = q.poll();
			int curR = a[0];
			int curC = a[1];

			for (int d = 0; d < 8; d++) {
				int newR = curR + dr[d];
				int newC = curC + dc[d];
				if ((newR < 0 || newR >= r) || (newC < 0 || newC >= c)) {
					continue;
				}
				if (graph[newR][newC] == 0 && visited[curR][curC] + 1 < visited[newR][newC]) {
					visited[newR][newC] = visited[curR][curC] + 1;
					q.offer(new int[] {newR, newC});
				}
			}
		}
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());

		graph = new int[r][c];
		shark = new ArrayList<>();

		for (int i = 0; i < r; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < c; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				if (graph[i][j] == 1) {
					shark.add(new int[]{i, j});
				}
			}
		}
	}
}
