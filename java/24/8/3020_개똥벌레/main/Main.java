import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int h;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        int[] top = new int[n/2];
        int[] bot = new int[n/2];

        for (int i = 0; i < n/2; i++) {
            bot[i] = Integer.parseInt(br.readLine());
            top[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(bot);
        Arrays.sort(top);

        int[] resultAry = new int[h];

        int minVal = n;
        int sameVal = 0;

        for (int i = 0; i < h; i++) {
            resultAry[i] = (n / 2) - lowerBound(top, i + 1)
                    + (n / 2) - lowerBound(bot, h - i);

            if (resultAry[i] == minVal) {
                sameVal ++;
                continue;
            }
            if (resultAry[i] < minVal) {
                minVal = resultAry[i];
                sameVal = 1;
            }
        }

        System.out.println(minVal + " " + sameVal);
    }

    private static int lowerBound(int[] ary, int target) {
        int left = 0;
        int right = ary.length;

        while (left < right) {
            int mid = (left + right) / 2;

            if (ary[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}