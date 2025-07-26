import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int[] ary;
	static int n;
	// 회전초밥 접시 개수
	static int d;
	// 초밥 가짓수
	static int k;
	// 연속해서 먹는 접시 수
	static int c;
	// 보너스 초밥
	
	static HashSet<Integer> hash;
	static int result;

	public static void main(String[] args) throws IOException {
		input();

		// solve sliding window
		// window size is k;
		// for문 한 요소씩 돌면서 이중 for 문으로 k 개까지 확인하면서 result 갱신해주기;
		// result 갱신은 hashset 써서 초밥이 중복됐는지 확인하고 길이 확인하기 그리고 보너스초밥
		// c가 해당 안되어 있다면 + 1 해주기

		result = 0;
		for (int i = 0; i < n; i++) {
			int cnt = 0;
			int curIdx = i;
			hash = new HashSet<>();

			for (int j = 0; j < k; j++) {
				if (curIdx >= n) {
					curIdx = 0;
				}
				hash.add(ary[curIdx]);
				curIdx++;
			}
			hash.add(c);

			result = Math.max(result, hash.size());
		}

		System.out.println(result);
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		ary = new int[n];

		for (int i = 0; i < n; i++) {
			ary[i] = Integer.parseInt(br.readLine());
		}
	}
}
