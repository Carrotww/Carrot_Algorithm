import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int n;
	static int[] ary;

	public static void main(String[] args) throws IOException {
		input();
		int result = 0;
		Arrays.sort(ary);

		for (int i = 0; i < n; i++) {
			int target = ary[i];
			int start = 0;
			int end = n - 1;

			while (start < end) {
				if (start == i) {
					start ++;
					continue;
				}
				if (end == i) {
					end --;
					continue;
				}
				if (ary[start] + ary[end] == target) {
					result++;
					break;
				} else if (ary[start] + ary[end] < target) {
					start++;
				} else {
					end--;
				}
			}
		}

		System.out.println(result);
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		ary = new int[n];
		for (int i = 0; i < n; i++) {
			ary[i] = Integer.parseInt(st.nextToken());
		}
	}
}
