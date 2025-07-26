
import java.util.*;
import java.io.*;

public class Main2 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		List<int[]> ary = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int front = Integer.parseInt(st.nextToken());
			int last = Integer.parseInt(st.nextToken());
			ary.add(new int[] {front, 1});
			ary.add(new int[] {last, -1});
		}

		int result = 0;
		int total = 0;

		ary.sort((o1, o2) -> {
			if (o1[0] != o2[0]) return Integer.compare(o1[0], o2[0]);
			return Integer.compare(o1[1], o2[1]);
		});

		for (int[] t : ary) {
			total += t[1];
			result = Math.max(result, total);
		}

		System.out.println(result);
	}
}

