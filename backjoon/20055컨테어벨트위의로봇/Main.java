
import java.util.*;
import java.io.*;

class Box {
	int cnt;
	boolean isRobot;

	public Box (int c, boolean r) {
		this.cnt = c;
		this.isRobot = r;
	}
}

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int N;
	static int K;
	static Deque<Box> conTop = new LinkedList<>();
	static Deque<Box> conBot = new LinkedList<>();

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
			// 1
			// n-1 번째 로봇은 없어져야 함
			// 돌리면 됨

			result++;

			Box lastBox = conTop.pollLast();
			lastBox.isRobot = false;
			conBot.addFirst(lastBox);

			Box firstBox = conBot.pollLast();
			conTop.addFirst(firstBox);

			// 2
			Box lastBox2 = conTop.pollLast();
			lastBox2.isRobot = false;
			conTop.addLast(lastBox2);

			for (int i = 0; i < N - 1; i++) {
				Box curBox = conTop.pollLast();
				Box prevBox = conTop.pollLast();

				if (prevBox == null || curBox == null) {
					System.out.println(totalCnt);
					System.out.println("Null 발생 직전: prev=" + prevBox + ", cur=" + curBox);
				}

				if (prevBox.isRobot && !curBox.isRobot && curBox.cnt > 0) {
					curBox.isRobot = true;
					curBox.cnt--;
					prevBox.isRobot = false;

					if (curBox.cnt == 0) {
						totalCnt++;
					}
				}

				conTop.addFirst(curBox);
				conTop.addLast(prevBox);
			}

			conTop.addFirst(conTop.pollLast());

			// 3
			Box firstBox3 = conTop.pollFirst();
			if (firstBox3.cnt > 0) {
				firstBox3.cnt--;
				firstBox3.isRobot = true;

				if (firstBox3.cnt == 0) {
					totalCnt++;
				}
			}
			conTop.addFirst(firstBox3);

			// 4
			if (totalCnt >= K) {
				break;
			}
		}

		System.out.println(result);
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			int cnt = Integer.parseInt(st.nextToken());
			conTop.add(new Box(cnt, false));
		}

		for (int i = 0; i < N; i++) {
			int cnt = Integer.parseInt(st.nextToken());
			conBot.add(new Box(cnt, false));
		}
	}
}
