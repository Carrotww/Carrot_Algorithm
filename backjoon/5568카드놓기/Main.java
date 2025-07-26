
import java.util.*;
import java.io.*;

public class Main {
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
			int[] visited = new int[K];
			List<Integer> temp2 = new ArrayList<Integer>();
			permutation(temp, visited, temp2);
			return;
		}

		for (int i = index; i < N; i++) {
			temp.add(ary[i]);
			backtracking(i + 1, temp);
			temp.remove(temp.size() - 1);
		}
	}

	public static void permutation(List<Integer> inputAry, int[] visited, List<Integer> temp) {
		if (temp.size() == K) {
			int number = 0;
			for (int val : temp) {
				int len = String.valueOf(val).length();
				number = number * (int) Math.pow(10, len) + val;
			}
			hash.add(number);
			return;
		}

		for (int i = 0; i < K; i++) {
			if (visited[i] == 0) {
				visited[i] = 1;
				temp.add(inputAry.get(i));
				permutation(inputAry, visited, temp);
				visited[i] = 0;
				temp.remove(temp.size() - 1);
			}
		}
	}
}
