import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) ->  {
			if (a[0] == b[0]) {
				return Integer.compare(a[1], b[1]);
			}
			return Integer.compare(a[0], b[0]);
		});

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int P = Integer.parseInt(st.nextToken());
			int L = Integer.parseInt(st.nextToken());

			pq.add(new int[]{L, P});
		}

		st = new StringTokenizer(br.readLine());
		int m = Integer.parseInt(st.nextToken());

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			String command = st.nextToken();

			if (command.equals("add")) {
				int P = Integer.parseInt(st.nextToken());
				int L = Integer.parseInt(st.nextToken());

				pq.add(new int[]{L, P});

			} else if (command.equals("recommend")) {
				if (Integer.parseInt(st.nextToken()) == 1) {
					// 어려운 난이도 문제 출력
					pq.poll()
				} else {
					// 쉬운 난이도 문제 출력
				}

			} else {
				//solve
				int P = Integer.parseInt(st.nextToken());
				System.out.println("solve");
			}
		}
	}
}
