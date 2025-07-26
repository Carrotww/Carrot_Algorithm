import java.util.*;
import java.io.*;

public class Main2 {

	static BufferedReader br;
	static StringTokenizer st;
	static int n;
	static int d;
	static int k;
	static int c;
	static int[] ary;
	static int result;
	static HashMap<Integer, Integer> hash;

	public static void main(String[] args) throws IOException {
		input();
		
		hash = new HashMap<>();
		hash.put(c, 1);

		// init
		for (int i = 0; i < k; i++) {
			if (hash.containsKey(ary[i])) {
				hash.put(ary[i], hash.get(ary[i]) + 1);
			} else {
				hash.put(ary[i], 1);
			}
		}
		result = hash.size();

		// first, write pop logic and write push logic
		for (int i = 0; i < n - 1; i++) {
			int popIdx = i;
			int pushIdx = (i + k) % n; 

			hash.put(ary[popIdx], hash.get(ary[popIdx]) - 1);
			if (hash.get(ary[popIdx]) == 0) {
				hash.remove(ary[popIdx]);
			}

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
