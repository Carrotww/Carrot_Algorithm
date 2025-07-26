import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int T;
	static int N;
	static int K;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		T = Integer.parseInt(st.nextToken());
		for (int i = 0; i < T; i++) {
			solve();
		}
	}

	public static void solve() throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		int[] ary = new int[N];

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) ary[i] = Integer.parseInt(st.nextToken());

		Arrays.sort(ary);

		int cnt = twoPointer(ary, K);
		System.out.println(cnt);
	}

	public static int twoPointer(int[] ary, int target) {
		int cnt = 0;
		int start = 0;
		int end = ary.length - 1;
		int closeValue = Integer.MAX_VALUE;

		while (start < end) {
			int sum = ary[start] + ary[end];
			int diff = Math.abs(sum - target);

			if (diff < closeValue) {
				cnt = 1;
				closeValue = diff;
			} else if (diff == closeValue) {
				cnt++;
			}

			if (sum < target) {
				start++;
			} else if (sum > target) {
				end--;
			} else {
				start++;
			}
		}

		return cnt;
	}
}
