import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int n;
	static int x;
	static int[] ary;

	public static void main(String[] args) throws IOException {
		input();
		// 정렬 하고 투포인터로 풀면 된다
		Arrays.sort(ary);

		int start, end, result;
		start = 0;
		end = n - 1;
		result = 0;

		while (start < end) {
			int value = ary[start] + ary[end];
			if (value == x) {
				result ++;
				start++;
			} else if (value < x) {
				start ++;
			} else {
				end --;
			}
		}

		System.out.println(result);
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		x = Integer.parseInt(br.readLine());
		ary = new int[n];

		for (int i = 0; i < n; i++) {
			ary[i] = Integer.parseInt(st.nextToken());
		}
	}
}
