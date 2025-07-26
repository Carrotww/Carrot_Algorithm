import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) {

	}

	public static int binarySearch(int[] ary, int target) {
		int start = 0;
		int end = ary.length - 1;

		while (start <= end) {
			int mid = (start + end) / 2;

			if (ary[mid] == target) {
				return mid;
			} else if (ary[mid] < target) {
				start = mid + 1;
			} else {
				end = mid - 1;
			}
		}
		return -1;
	}

	public static int lowerBound(int[] ary, int target) {
		int start = 0;
		int end = ary.length;

		while (start < end) {
			int mid = (start + end) / 2;

			if (ary[mid] < target) {
				start = mid + 1;
			} else {
				end = mid;
			}
		}

		return start;
	}

	public static int upperBound(int[] ary, int target) {
		int start = 0;
		int end = ary.length;

		while (start < end) {
			int mid = (start + end) / 2;

			if (ary[mid] <= target) {
				start = mid + 1;
			} else {
				end = mid;
			}
		}

		return start;
	}
}
