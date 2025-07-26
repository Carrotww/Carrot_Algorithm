
import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());

		String[] a = new String[n];
		String[] b = new String[n];

		for (int i = 0; i < n; i++) {
			String t = br.readLine();
			a[i] = t;
		}

		for (int i = 0; i < n; i++) {
			String t = br.readLine();
			b[i] = t;
		}

		int cnt = 0;

		System.out.println(Arrays.toString(a));
		System.out.println(Arrays.toString(b));

		for (int i = 0; i < n; i++) {
			Set<String> set = new HashSet<>();
			for (int j = 0; j < i; j++) {
				set.add(a[j]);
			}
			System.out.println(set);

			for (int z = i + 1; z < n; z++) {
				if (set.contains(b[z])) {
					cnt++;
					break;
				}
			}
		}

		System.out.println(cnt);
	}
}
