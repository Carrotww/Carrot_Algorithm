import java.util.*;
import java.io.*;

public class Main2 {
	static BufferedReader br;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();

		Stack<Character> stack = new Stack<>();

		for (char c : input.toCharArray()) {
			if (c == '(') {
				stack.add(c);
			} else {
				if (!stack.isEmpty() && stack.peek() == '(') {
					stack.pop();
				} else {
					stack.add(c);
				}
			}
		}

		System.out.println(stack.size());
	}
}
