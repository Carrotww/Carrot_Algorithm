
import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());

		String[] input = new String[n];
		String[] output = new String[n];
		Map<String, List<Integer>> map = new HashMap<>();

		for (int i = 0; i < n; i++) {
			String t = br.readLine();
			List<Integer> a = new ArrayList<>();
			input[i] = t;
			a.add(i);
			map.put(t, a);
		}

		for (int i = 0; i < n; i++) {
			String t = br.readLine();
			List<Integer> a = map.get(t);
			output[i] = t;
			a.add(i);
			map.put(t, a);
		}

		int cnt = 0;

		for (int i = 0; i < n; i++) {
			// 앞에 있는 것부터 돌아서 지금 내 앞에 있는 것들이 나중에 뒤에 있으면 재낀거임
			// 앞에 있는 애들을 for 문으로 돌아서 output 인덱스를 찾아서 set으로 만들어 줘 일단
			// 1. output 인덱스를 찾아서 뒤에 애들을 set으로 만들어줌
			// 2. input 앞부분을 돌면서 output에 있으면 cnt ++

			int outputIdx = map.get(input[i]).get(1);

			Set<String> set = new HashSet<>();
			for (int o = outputIdx; o < n; o++) {
				set.add(output[o]);
			}

			// set 만들어 주었으니 이제 확인
			for (int j = 0; j < i; j++) {
				if (set.contains(input[j])) {
					cnt++;
					break;
				}
			}
		}

		System.out.println(cnt);
	}
}
