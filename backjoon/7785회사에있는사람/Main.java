import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		HashMap<String, String> hash = new HashMap<>();

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			String name = st.nextToken();
			String path = st.nextToken();

			if (path.equals("enter")) {
				hash.put(name, name);
			} else {
				hash.remove(name);
			}
		}

		List<String> ary = new ArrayList<>(hash.keySet());
		Collections.sort(ary, Collections.reverseOrder());

		for (String s : ary) {
			System.out.println(s);
		}
	}
}
