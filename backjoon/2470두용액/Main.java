import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int n;
	static int[] ary;

	public static void main(String[] args) throws IOException {
		input();
		Arrays.sort(ary);

		// 풀이
		// 1. 절대값으로 계산할 것이니 초기 값 2000000000으로 result 선언
		// 2. 투포인터로 계산하며 result를 갱신해준다.

		int sum = 2000000000;
		int result1 = 0;
		int result2 = 0;
		
		int start = 0;
		int end = n - 1;

		while (start < end) {
			int val = ary[start] + ary[end];

			if (Math.abs(val) < sum) {
				result1 = ary[start];
				result2 = ary[end];
				sum = Math.abs(val);
			}

			if (val < 0) {
				start++;
			} else if (val > 0) {
				end--;
			} else {
				break;
			}
		}

		System.out.println(result1 + " " + result2);
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
