
import java.util.*;
import java.io.*;

public class Main {
	static int n;
	static int r;
	static BufferedReader br;
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			r = Integer.parseInt(st.nextToken());

			if (n == 0 && r == 0) {
				break;
			}

			long result = combination();
			System.out.println(result);
		}
	}

	public static long combination() {
		long sum = 1;
		if (r > n - r) r = n - r;

		for (int i = 1; i <= r; i++) {
			sum = sum * (n - i + 1) / i;
		}

		return sum;
	}
}
