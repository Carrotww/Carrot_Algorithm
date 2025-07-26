
import java.util.*;
import java.io.*;

class Node {
	int front;
	int last;

	public Node(int f, int l) {
		this.front = f;
		this.last = l;
	}
}

public class Main {
	static BufferedReader br;
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		List<int[]> ary = new ArrayList<>();

		PriorityQueue<Integer> pLast = new PriorityQueue<>();

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int front = Integer.parseInt(st.nextToken());
			int last = Integer.parseInt(st.nextToken());
			ary.add(new int[] {front, last});
		}

		ary.sort((o1, o2) -> {
			if (o1[0] != o2[0]) return Integer.compare(o1[0], o2[0]);
			return Integer.compare(o1[1], o2[1]);
		});

		// ary.sort(Comparator.comparingInt((int[] o) -> o[0]).thenComparingInt((int[] o) -> o[1]));

		int result = 1;

		for (int i = 0; i < ary.size(); i++) {
			int[] cur = ary.get(i);

			while (!pLast.isEmpty() && pLast.peek() <= cur[0]) {
				pLast.poll();
			}

			pLast.add(cur[1]);
			result = Math.max(result, pLast.size());
		}

		System.out.println(result);
	}
}
