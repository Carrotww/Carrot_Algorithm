
import java.util.*;
import java.io.*;

public class Main2 {
	static BufferedReader br;
	static StringTokenizer st;
	static int N;
	static int L;
	static int[][] graph;

	public static void main(String[] args) throws IOException {
		input();

		int cnt = 0;

		for (int i = 0; i < N; i++) {
			int[] temp = new int[N];
			for (int j = 0; j < N; j++) {
				temp[j] = graph[i][j];
			}
			cnt += solve(temp);
			for (int z = 0; z < N; z++) {
				temp[z] = graph[z][i];
			}
			cnt += solve(temp);
		}

		System.out.println(cnt);
	}

	public static int solve(int[] ary) {

		int cnt = 1;

		for (int i = 0; i < N - 1; i++) {
			int cur = ary[i];
			int next = ary[i + 1];

			// down
			if (cur - next == 1) {
				for (int j = 0; j < L; j++) {
					int idx = i + j + 1;
					if (idx >= N || ary[idx] != next) return 0;
				}
				i += L - 1;
				cnt = 0;
			// up
			} else if (cur - next == -1) {
				if (cnt < L) {
					return 0;
				}
				cnt = 1;

			} else if (cur == next) {
				cnt++;
			} else {
				return 0;
			}
		}

		return 1;
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		L = Integer.parseInt(st.nextToken());

		graph = new int[N][N];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
	}

}
