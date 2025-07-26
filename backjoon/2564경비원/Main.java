
import java.util.*;
import java.io.*;

public class Main {
	static int result;
	static int r;
	static int c;
	static BufferedReader br;
	static StringTokenizer st;
	static List<Integer> list;
	static int startP;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		c = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		
		list = new ArrayList<>();

		// 북 dist
		// 남 r + c + (c - dist)
		// 서 r + c * 2 + (r - dist)
		// 동 c + dist

		int totalSize = r * 2 + c * 2;

		for (int i = 0; i < n + 1; i++) {
			st = new StringTokenizer(br.readLine());
			int direct = Integer.parseInt(st.nextToken());
			int dist = Integer.parseInt(st.nextToken());

			if (direct == 1) {
				list.add(dist);
			} else if (direct == 2) {
				list.add(r + c + (c - dist));
			} else if (direct == 3) {
				list.add(r + c * 2 + (r - dist));
			} else {
				list.add(c + dist);
			}
		}

		startP = list.get(n);

		for (int i = 0; i < n; i++) {
			int curP = list.get(i);
			// start 가 앞에 있을 때
			// curP - start, totalSize - curP + start
			//
			// start 가 뒤에 있을 때

			if (startP < curP) {
				result += Math.min(curP - startP, totalSize - curP + startP);
			} else {
				result += Math.min(startP - curP, totalSize - startP + curP);
			}
		}

		System.out.println(result);
	}
}
