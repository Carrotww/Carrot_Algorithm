import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();

		char[] ary = input.toCharArray();
		int close = 0;
		int open = 0;
		for (int i = ary.length - 1; i >= 0; i--) {
			if (ary[i] == ')') {
				close++;
			} else {
				if (close > 0) {
					close--;
				} else {
					open++;
				}
			}
		}
		System.out.println(close + open);
	}
}
