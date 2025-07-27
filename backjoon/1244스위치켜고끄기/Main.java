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
				for (int j = num; j < N + 1; j += num) {
					if (sw[j - 1] == 0) {
						sw[j - 1] = 1;
					} else {
						sw[j - 1] = 0;
					}
				}
			} else {
				num--;
				int right = num;
				int left = num;
				int maxR = num;
				int minL = num;

				while (right < N && left >= 0) {
					if (sw[right] == sw[left]) {
						maxR = right;
						minL = left;
					} else {
						break;
					}
					right++;
					left--;
				}

				for (int z = minL; z <= maxR; z++) {
					if (sw[z] == 0) {
						sw[z] = 1;
					} else {
						sw[z] = 0;
					}
				}
			}
		}
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < N; i++) {
			sb.append(sw[i]).append(" ");
			if ((i + 1) % 20 == 0) {
				sb.append("\n");
			}
		}
		System.out.println(sb);
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
