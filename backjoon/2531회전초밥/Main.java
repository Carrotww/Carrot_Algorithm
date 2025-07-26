import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int[] ary;
	static int n;
	// 회전초밥 접시 개수
	static int d;
	// 초밥 가짓수
	static int k;
	// 연속해서 먹는 접시 수
	static int c;
	// 보너스 초밥
	
	static HashSet<Integer> hash;
	static int result;

	public static void main(String[] args) throws IOException {
		input();

		HashMap<Integer, Integer> hash = new HashMap<>();

		hash.put(c, 1);

		for (int i = 0; i < k; i++) {
			if (!hash.containsKey(ary[i])) {
				hash.put(ary[i], 1);
			} else {
				hash.put(ary[i], hash.get(ary[i]) + 1);
			}
		}

		result = hash.size();

		for (int i = 0; i < n - 1; i++) {
			hash.put(ary[i], hash.get(ary[i]) - 1);
			if (hash.get(ary[i]) == 0) {
				hash.remove(ary[i]);
			}

			int pushIdx = (i + k) % n;

			if (hash.containsKey(ary[pushIdx])) {
				hash.put(ary[pushIdx], hash.get(ary[pushIdx]) + 1);
			} else {
				hash.put(ary[pushIdx], 1);
			}

			result = Math.max(result, hash.size());
		}
		System.out.println(result);
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		ary = new int[n];

		for (int i = 0; i < n; i++) {
			ary[i] = Integer.parseInt(br.readLine());
		}
	}
}
