
import java.util.*;
import java.io.*;

public class Main {
	static int n;
	static int[] ary;
	static int maxResult = Integer.MIN_VALUE;
	static int minResult = Integer.MAX_VALUE;
	static int[] cal = new int[4];
	static BufferedReader br;
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());

		ary = new int[n];

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			ary[i] = Integer.parseInt(st.nextToken());
		}

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < 4; i++) {
			cal[i] = Integer.parseInt(st.nextToken());
		}

		dfs(0, ary[0], cal[0], cal[1], cal[2], cal[3]);

		System.out.println(maxResult);
		System.out.println(minResult);
	}

	public static void dfs(int idx, int sum, int plus, int minus, int multiply, int divide) {
		if (idx == n - 1) {
			maxResult = Math.max(maxResult, sum);
			minResult = Math.min(minResult, sum);

			return;
		}

		if (plus > 0) {
			dfs(idx + 1, sum + ary[idx + 1], plus - 1, minus, multiply, divide);
		}
		if (minus > 0) {
			dfs(idx + 1, sum - ary[idx + 1], plus, minus - 1, multiply, divide);
		}
		if (multiply > 0) {
			dfs(idx + 1, sum * ary[idx + 1], plus, minus, multiply - 1, divide);
		}
		if (divide > 0) {
			dfs(idx + 1, sum / ary[idx + 1], plus, minus, multiply, divide - 1);
		}
	}
}
