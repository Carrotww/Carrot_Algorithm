
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();

        System.out.println(s.solution(22, 6, 8));
        System.out.println(s.solution(13, 3, 6));
        // 4
    }
}

class Solution {
    public int solution(int n, int w, int num) {
        int r = (n + w - 1) / w;
        int c = w;

        int[][] graph = new int[r][c];
        int val = 1;
        int right = 1;

        for (int i = 0; i < r; i++) {
            if (right == 1) {
                for (int j = 0; j < c; j++) {
                    if (val > n) break;
                    graph[i][j] = val++;
                }
                if (val > n) break;
                right *= -1;
            } else {
                for (int j = c - 1; j >= 0; j--) {
                    if (val > n) break;
                    graph[i][j] = val++;
                }
                if (val > n) break;
                right *= -1;
            }
        }

        int numR = -1;
        int numC = -1;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (graph[i][j] == num) {
                    numR = i;
                    numC = j;
                }
            }
        }


        int top = (graph[r - 1][numC] != 0) ? (r - 1) : (r - 2);
        int result = top - numR + 1;
        
        return result;
    }
}