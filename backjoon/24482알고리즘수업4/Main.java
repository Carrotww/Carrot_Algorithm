
import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int N;
	static int M;
	static int R; // start node
	static int[] visited;
	static List<Integer>[] graph;

	public static void main(String[] args) throws IOException {
		input();
		dfs(R);

		for (int i = 1; i < N + 1; i++) {
			if (visited[i] != 0 || i == R) {
				System.out.println(visited[i]);
			} else {
				System.out.println(-1);
			}
		}
	}

	public static void dfs(int node) {
		for (int i = 0; i < graph[node].size(); i++) {
			int nNode = graph[node].get(i);

			if (visited[nNode] == 0 && nNode != R) {
				visited[nNode] = visited[node] + 1;
				dfs(nNode);
			}
		}
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());

		graph = (ArrayList<Integer>[]) new ArrayList[N + 1];
		visited = new int[N + 1];

		for (int i = 0; i < N + 1; i++) {
			graph[i] = new ArrayList<Integer>();
		}

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a, b;
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			graph[a].add(b);
			graph[b].add(a);
		}

		for (int i = 1; i < N + 1; i++) {
			graph[i].sort(Collections.reverseOrder());
		}
	}
}
