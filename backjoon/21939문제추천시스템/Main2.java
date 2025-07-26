import java.util.*;
import java.io.*;

class Node {
	int idx;
	int level;

	Node(int idx, int level) {
		this.idx = idx;
		this.level = level;
	}

	@Override
	public String toString() {
		return "(" + "idx : " + idx + ", " + "level : " + level + ")";
	}
}

// priority queue solve
public class Main2 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());

		// 쉬운 문제
		PriorityQueue<Node> heapAsc = new PriorityQueue<>(new Comparator<Node>() {
			@Override
			public int compare(Node n1, Node n2) {
				if (n1.level != n2.level) return Integer.compare(n1.level, n2.level);
				return Integer.compare(n1.idx, n2.idx);
			}
		});

		// 어려운 문제
		PriorityQueue<Node> heapDes = new PriorityQueue<>(new Comparator<Node>() {
			@Override
			public int compare(Node n1, Node n2) {
				if (n1.level != n2.level) return Integer.compare(n2.level, n1.level);
				return Integer.compare(n2.idx, n1.idx);
			}
		});

		HashMap<Integer, Integer> hash = new HashMap<>();

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int P = Integer.parseInt(st.nextToken());
			int L = Integer.parseInt(st.nextToken());

			hash.put(P, L);
			heapAsc.add(new Node(P, L));
			heapDes.add(new Node(P, L));
		}

		st = new StringTokenizer(br.readLine());
		int m = Integer.parseInt(st.nextToken());

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			String command = st.nextToken();

			switch(command) {
				case "add":
					int P = Integer.parseInt(st.nextToken());
					int L = Integer.parseInt(st.nextToken());
					hash.put(P, L);
					heapAsc.add(new Node(P, L));
					heapDes.add(new Node(P, L));
					break;

				case "recommend":
					int level = Integer.parseInt(st.nextToken());
					if (level == 1) {
						while (!hash.containsKey(heapDes.peek().idx) || (heapDes.peek().level != hash.get(heapDes.peek().idx))) {
							heapDes.poll();
						}
						System.out.println(heapDes.peek().idx);
					} else {
						while (!hash.containsKey(heapAsc.peek().idx) || (heapAsc.peek().level != hash.get(heapAsc.peek().idx))) {
							heapAsc.poll();
						}
						System.out.println(heapAsc.peek().idx);
					}
					break;

				default:
					P = Integer.parseInt(st.nextToken());
					hash.remove(P);
			}
		}
	}
}
