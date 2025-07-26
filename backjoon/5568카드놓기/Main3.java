
import java.util.*;
import java.io.*;

public class Main3 {
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

		combination(0, new ArrayList<>());

		System.out.println(hash.size());
	}

	public static void combination(int index, List<Integer> valueList) {

		if (valueList.size() == K) {
			int[] visited = new int[valueList.size()];
			permutation(valueList, visited, new ArrayList<>());
			return;
		}

		for (int i = index; i < N; i++) {
			valueList.add(ary[i]);
			combination(i + 1, valueList);
			valueList.remove(valueList.size() - 1);
		}

		return;
	}

	public static void permutation(List<Integer> inputAry, int[] visited, List<Integer> valueList) {
		if (valueList.size() == K) {
			int number = 0;

			for (int val : valueList) {
				number = number * (int)Math.pow(10, String.valueOf(val).length()) + val;
			}
			hash.add(number);
			return;
		}

		for (int i = 0; i < K; i++) {
			if (visited[i] == 0) {
				visited[i] = 1;
				valueList.add(inputAry.get(i));
				permutation(inputAry, visited, valueList);
				visited[i] = 0;
				valueList.remove(valueList.size() - 1);
			}
		}
	}
}
