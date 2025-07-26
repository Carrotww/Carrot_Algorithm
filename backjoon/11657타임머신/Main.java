import java.util.*;
import java.io.*;

class Node {
	int start;
	int end;
	int cost;

	public Node(int start, int end, int cost) {
		this.start = start;
		this.end = end;
		this.cost = cost;
	}
}

public class Main {

	static BufferedReader br;
	static StringTokenizer st;
	static List<Node> graph = new ArrayList<>();
	static long[] dist;
	static List<Long> result = new ArrayList<>();
	static int n;
	static int m;
	static int MAX_VALUE = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		dist = new long[n + 1];
		Arrays.fill(dist, MAX_VALUE);
		dist[1] = 0;

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			int cost = Integer.parseInt(st.nextToken());

			graph.add(new Node(start, end, cost));
		}

		bellmanford();

		for (long r : result) {
			System.out.println(r);
		}
	}

	public static void bellmanford() {
		for (int i = 1; i < n; i++) {
			for (Node node : graph) {
				int start = node.start;
				int end = node.end;
				int cost = node.cost;

				if (dist[start] != MAX_VALUE && dist[start] + cost < dist[end]) {
					dist[end] = dist[start] + cost;
				}
			}
		}

		for (Node node : graph) {
			int start = node.start;
			int end = node.end;
			int cost = node.cost;

			if (dist[start] != MAX_VALUE && dist[start] + cost < dist[end]) {
				dist[end] = dist[start] + cost;
				result.add((long) -1);
				return;
			}
		}

		for (int i = 2; i < n + 1; i++) {
			if (dist[i] == MAX_VALUE) {
				result.add((long) -1);
			} else {
				result.add(dist[i]);
			}
		}
	}
}
