
import java.io.*;
import java.util.*;

public class Permutation {

	static int[] ary = {1, 2, 3, 4, 5};
	static List<Integer> output = new ArrayList<>();
	static boolean[] visited;
	static int target;

	public static void main(String[] args) {
		visited = new boolean[ary.length];
		target = 2;

		permutation();
	}

	public static void permutation() {
		if (output.size() == target) {
			System.out.println(output);
			return;
		}

		for (int i = 0; i < ary.length; i++) {
			if (!visited[i]) {
				output.add(ary[i]);
				visited[i] = true;
				permutation();
				output.remove(output.size() - 1);
				visited[i] = false;
			}
		}
	}
}
