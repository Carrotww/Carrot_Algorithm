import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nn = br.readLine();
        String mm = br.readLine();
        String n_ary = br.readLine();

        int n = Integer.parseInt(nn);
        int m = Integer.parseInt(mm);

        String[] n_ary_str = n_ary.split(" ");
        int[] ary = new int[n];

        for (int i = 0; i < n; i++) {
            ary[i] = Integer.parseInt(n_ary_str[i]);
        }
        Arrays.sort(ary);

        int left = 0;
        int right = n - 1;
        int result = 0;

        while (left < right) {
            int cur_val = ary[left] + ary[right];
            if (cur_val == m) {
                result ++;
                left ++;
                right --;
            }
            else if (cur_val < m) {
                left ++;
            }
            else {
                right --;
            }
        }
        System.out.println(result);
    }
}
