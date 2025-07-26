
import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int n;
	static int m;
	static ArrayList<ArrayList<Integer>> graph;
	static int[] indegree;
	static int[] result;

	public static void main(String[] args) throws IOException {
		input();

		topologySort();

		StringBuilder sb = new StringBuilder();
		for (int i = 1; i < n + 1; i++) {
			sb.append(result[i]).append(" ");
		}
		System.out.println(sb);
	}

	public static void topologySort() {
		Queue<Integer> q = new LinkedList<>();

		for (int i = 1; i < n + 1; i++) {
			if (indegree[i] == 0) {
				q.add(i);
				result[i] = 1;
			} 
		}

		while (!q.isEmpty()) {
			int cur = q.poll();

			for (int next : graph.get(cur)) {
				indegree[next]--;

				if (indegree[next] == 0) {
					result[next] = result[cur] + 1;
					q.add(next);
				}
			}
		}
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		graph = new ArrayList<ArrayList<Integer>>();
		indegree = new int[n + 1];
		result = new int[n + 1];

		for (int i = 0; i < n + 1; i++) {
			graph.add(new ArrayList<>());
		}

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			graph.get(a).add(b);
			indegree[b]++;
		}
	}
}
