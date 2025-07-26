
import java.util.*;
import java.io.*;

public class JoinIntArray {
	static int[] ary2 = {4, 5, 12, 99};
	static int[] ary = {4, 5, 12, 999, 1, 20, 33};

	public static void main(String[] args) {
		joinIntArray();
	}

	public static void joinIntArray() {
		System.out.println(Arrays.toString(ary));

		long number = 0;
		for (int a : ary) {
			int len = String.valueOf(a).length();
			number = number * (long) Math.pow(10, len) + a;
		}
		System.out.println(number);
	}
}
