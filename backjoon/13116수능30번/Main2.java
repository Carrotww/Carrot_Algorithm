
import java.util.*;
import java.io.*;

public class Main2 {
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

		if (a == b) {
			System.out.println(a * 10);
			return;
		}

		while (a != b) {
			if (a > b) a /= 2;
			else b /= 2;
			if (a == b) {
				System.out.println(a * 10);
				break;
			}
		}
	}
}
