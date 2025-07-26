
import java.util.*;
import java.io.*;

public class Main2 {
	static BufferedReader br;
	static StringTokenizer st;
	static int N;
	static int K;
	static int[] belt;
	static boolean[] robot;

	public static void main(String[] args) throws IOException {
		// 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
		// 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
			// 2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
		// 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
		// 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

		input();

		int totalCnt = 0;
		int result = 0;

		while (true) {
			result++;
			// 1
			int tmp = belt[2 * N - 1];
			for (int i = 2 * N - 1; i > 0; i--) {
				belt[i] = belt[i - 1];
			}
			belt[0] = tmp;

			robot[N - 1] = false;
			for (int i = N - 1; i > 0; i--) {
				robot[i] = robot[i - 1];
			}
			robot[0] = false;

			// 2
			robot[N - 1] = false;
			for (int i = N - 1; i > 0; i--) {
				if (robot[i - 1] && !robot[i] && belt[i] > 0) {
					robot[i] = true;
					robot[i - 1] = false;
					belt[i]--;

					if (belt[i] == 0) totalCnt++;
				}
			}

			// 3
			if (!robot[0] && belt[0] > 0) {
				robot[0] = true;
				belt[0]--;
				if (belt[0] == 0) totalCnt++;
			}

			// 4
			if (totalCnt >= K) break;
		}

		System.out.println(result);
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());

		belt = new int[2 * N];
		robot = new boolean[N];

		for (int i = 0; i < 2 * N; i++) {
			belt[i] = Integer.parseInt(st.nextToken());
		}
	}
}
