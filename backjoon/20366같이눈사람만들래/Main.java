
import java.util.*;
import java.io.*;

class Node {
	int idxA;
	int idxB;
	int sum;

	public Node (int idxA, int idxB, int sum) {
		this.idxA = idxA;
		this.idxB = idxB;
		this.sum = sum;
	}
}

public class Main {
	static BufferedReader br;
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] ary = Arrays.stream(br.readLine().split(" "))
						.mapToInt(Integer::parseInt)
						.toArray();

		Arrays.sort(ary);
		// 4 <= N <= 600
		
		List<Node> aryList = new ArrayList<>();

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (i != j) {
					aryList.add(new Node(i, j, ary[i] + ary[j]));
				}
			}
		}

		// aryList.sort((o1, o2) -> Integer.compare(o1.sum, o2.sum));
		aryList.sort((Comparator.comparingInt(o -> o.sum)));

		int diff = Integer.MAX_VALUE;

		// for (int i = 0; i < aryList.size() - 1; i++) {
		// 	Node prev = aryList.get(i);
		// 	Node cur = aryList.get(i + 1);
		//
		// 	// if ((prev.idxA != cur.idxA) && (prev.idxB != cur.idxB) && (prev.idxA != cur.idxB) && (prev.idxB != cur.idxA)) {
		// 	// 	diff = Math.min(diff, cur.sum - prev.sum);
		// 	// }
		// }

		for (int i = 0; i < aryList.size() - 1; i++) {
			Node prev = aryList.get(i);
			for (int j = i + 1; j < aryList.size(); j++) {
				Node cur = aryList.get(j);

				if (diff <= cur.sum - prev.sum) break;

				if ((prev.idxA != cur.idxA) && (prev.idxB != cur.idxB) && (prev.idxA != cur.idxB) && (prev.idxB != cur.idxA)) {
					diff = Math.min(diff, cur.sum - prev.sum);
				}
			}
		}

		System.out.println(diff);
	}
}
