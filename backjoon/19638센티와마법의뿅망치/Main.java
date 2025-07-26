import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int N; // 거인의 수
	static int H; // 센티의 키
	static int T; // 망치 사용 횟수
	static PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

	public static void main(String[] args) throws IOException {
		input();
		int cnt = T;

		while (!pq.isEmpty() && T > 0) {
			int curP = pq.poll();
			if (curP == 1 || H > curP) {
				pq.add(curP);
				break;
			} else {
				curP /= 2;
				pq.add(curP);
				T--;
			}
		}

		if (pq.peek() < H) {
			System.out.println("YES");
			System.out.println(cnt - T);
		} else {
			System.out.println("NO");
			System.out.println(pq.poll());
		}
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());
		T = Integer.parseInt(st.nextToken());

		for (int i = 0; i < N; i++) {
			pq.add(Integer.parseInt(br.readLine()));
		}
	}
}
