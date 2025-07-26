
import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());

		int[] ary = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		int total = 0;

		for (int i = 0; i < X; i++) {
			total += ary[i];
		}

		int result = total;
		int cnt = 1;

		for (int i = X; i < N; i++) {
			total += ary[i] - ary[i - X];

			if (total > result) {
				result = total;
				cnt = 1;
			} else if (total == result) {
				cnt++;
			}
		}

		if (result != 0) {
			System.out.println(result);
			System.out.println(cnt);
		} else {
			System.out.println("SAD");
		}
	}
}
