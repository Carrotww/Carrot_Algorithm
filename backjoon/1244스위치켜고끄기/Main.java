import java.util.*;
import java.io.*;

public class Main {
	static int N;
	static int[] sw;
	static int P;
	static BufferedReader br;
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		input();

		for (int i = 0; i < P; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
			int num = Integer.parseInt(st.nextToken());

			if (s == 1) {
				for (int j = num; j < N + 1; j *= 2) {
					if (sw[j - 1] == 0) {
						sw[j - 1] = 1;
					} else {
						sw[j - 1] = 0;
					}
				}
			} else {
				int right = num + 1;
				int left = num - 1;
				int maxR = num;
				int minL = num;

				while (right <= N && left > 0) {
					if (right == left) {
						maxR = right;
						minL = num;
					}
					right++;
					left--;
				}

				if (maxR != num) {
					for (int z = minL; z < maxR; z++) {
						if (sw[z] == 0) {
							sw[z] = 1;
						} else {
							sw[z] = 0;
						}
					}
				}
			}

			System.out.println("cal time" + " " + i);
			System.out.println(Arrays.toString(sw));
		}

		System.out.println("result");
		System.out.println(Arrays.toString(sw));
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		sw = new int[N];

		for (int i = 0; i < N; i++) {
			sw[i] = Integer.parseInt(st.nextToken());
		}

		st = new StringTokenizer(br.readLine());
		P = Integer.parseInt(st.nextToken());
	}
}
