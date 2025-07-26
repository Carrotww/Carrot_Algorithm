
import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int t;
	static int a, b;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		t = Integer.parseInt(st.nextToken());
		for (int i = 0; i < t; i++) {
			solve();
		}
	}

	public static void solve() throws IOException {
		st = new StringTokenizer(br.readLine());
		a = Integer.parseInt(st.nextToken());
		b = Integer.parseInt(st.nextToken());

		Set<Integer> hash = new HashSet<>();

		while (a > 0) {
			hash.add(a);
			a /= 2;
		}

		while (b > 0) {
			if (hash.contains(b)) {
				System.out.println(b * 10);
				break;
			}
			b /= 2;
		}
	}
}
