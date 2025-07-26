
import java.util.*;
import java.io.*;

public class Main2 {
	static BufferedReader br;
	static StringTokenizer st;
	static int N;
	static int K;
	static int[] ary;
	static Set<Integer> hash = new HashSet<>();

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine());
		K = Integer.parseInt(br.readLine());

		ary = new int[N];
		for (int i = 0; i < N; i++) {
			ary[i] = Integer.parseInt(br.readLine());
		}

		backtracking(0, new ArrayList<>());

		System.out.println(hash.size());
	}

	public static void backtracking(int index, List<Integer> temp) {
		if (temp.size() == K) {
			boolean[] visited = new boolean[K]; // ✅ visited 제대로 초기화
			permutation(temp, visited, new ArrayList<>());
			return;
		}

		for (int i = index; i < N; i++) {
			temp.add(i);
			backtracking(i + 1, temp);
			temp.remove(temp.size() - 1);
		}
	}

	public static void permutation(List<Integer> indices, boolean[] visited, List<Integer> temp) {
		if (temp.size() == K) {
			// ✅ ary[index] 기준으로 숫자 만들기
			int number = 0;
			for (int idx : temp) {
				int val = ary[idx];
				int len = String.valueOf(val).length();
				number = number * (int)Math.pow(10, len) + val;
			}
			hash.add(number);
			return; // ✅ 종료 조건 누락 주의
		}

		for (int i = 0; i < K; i++) {
			if (!visited[i]) {
				visited[i] = true;
				temp.add(indices.get(i));
				permutation(indices, visited, temp);
				visited[i] = false;
				temp.remove(temp.size() - 1);
			}
		}
	}
}

