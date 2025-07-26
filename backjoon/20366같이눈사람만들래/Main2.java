
import java.util.*;
import java.io.*;

public class Main2 {
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

		// aryList.sort((o1, o2) -> Integer.compare(o1.sum, o2.sum));
		// aryList.sort((Comparator.comparingInt(o -> o.sum)));

		int diff = Integer.MAX_VALUE;

		for (int i = 0; i < n - 3; i++) {
			for (int j = n - 1; j > i + 2; j--) {
				int sum = ary[i] + ary[j];
				int start = i + 1;
				int end = j - 1;
				while (start < end) {
					int curSum = ary[start] + ary[end];
					diff = Math.min(diff, Math.abs(sum - curSum));
					if (curSum > sum) {
						end--;
					} else if (curSum < sum) {
						start++;
					} else {
						System.out.println(0);
						System.exit(0);
					}
				}
			}
		}

		System.out.println(diff);
	}
}
