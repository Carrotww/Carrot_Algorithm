
import java.util.*;
import java.io.*;

public class Combination {
	static int[] ary = {1, 2, 3, 4, 5};
	static List<Integer> output = new ArrayList<>();
	static int target;

	public static void main(String[] args) {
		target = 2;
		combination(0);
	}

	public static void combination(int index) {
		if (output.size() == target) {
			System.out.println(output);
			return;
		}

		for (int i = index; i < ary.length; i++) {
			output.add(ary[i]);
			combination(i + 1);
			output.remove(output.size() - 1);
		}
	}
}
