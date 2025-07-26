import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		String word = br.readLine();
		int result = 0;

		for (int i = 0; i < input.length(); i++) {
			int t_idx = i;

			if (t_idx + word.length() <= input.length()) {
				for (int j = 0; j < word.length(); j++) {
					if (input.charAt(t_idx) == word.charAt(j)) {
						t_idx++;
					} else {
						break;
					}
				}
			} else {
				break;
			}

			if (t_idx == i + word.length()) {
				result ++;
				i = t_idx - 1;
			}
		}

		System.out.println(result);
	}
}
