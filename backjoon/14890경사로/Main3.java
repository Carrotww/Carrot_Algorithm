
import java.util.*;
import java.io.*;

public class Main3 {
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
		int prev = ary[0];

		for (int i = 1; i < N; i++) {
			int cur = ary[i];
			if (prev == cur) {
				cnt++;
				// 내리막
				// 앞으로 내리막이 얼마나 있는지 L 만큼 for문 돌아야 함
				// 내리막에 L 만큼 경사로를 깔았으니 cnt = 0 이 되어야 함
				// 끝나면 i index 조정해주어야 함
			} else if (prev - cur == 1) {
				for (int j = 0; j < L; j++) {
					int idx = i + j;
					if (idx >= N || cur != ary[idx]) return 0;
				}
				cnt = 0;
				i += L - 1;
				prev = cur;
				// 오르막
				// cnt = 1 로 바꿔줌
				// prev 도 바꿔줌
			} else if (prev - cur == -1) {
				if (cnt < L) return 0;
				cnt = 1;
				prev = cur;
				// 2칸 이상 차이나는 케이스임
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
