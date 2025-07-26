
import java.util.*;
import java.io.*;

public class Main3 {
	static BufferedReader br;
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] ary = Arrays.stream(br.readLine().split(" "))
						.mapToInt(Integer::parseInt)
						.toArray();

		Arrays.sort(ary);
		int result = twoPointer(ary, Integer.MAX_VALUE);

		System.out.println(result);
	}

	public static int twoPointer(int[] ary, int diff) {
		int n = ary.length;

		for (int i = 0; i < n - 3; i++) {
			for (int j = n - 1; j > i + 2; j--) {
				int outSum = ary[i] + ary[j];

				int left = i + 1;
				int right = j - 1;

				while (left < right) {
					int innerSum = ary[left] + ary[right];
					if (outSum < innerSum) {
						right--;
					} else if (outSum > innerSum) {
						left++;
					} else {
						return 0;
					}
					diff = Math.min(diff, Math.abs(outSum - innerSum));
				}
			}
		}

		return diff;
	}
}
