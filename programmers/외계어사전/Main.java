import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(args, args));
    }
}

class Solution {
    public int solution(String[] spell, String[] dic) {
        // spell을 모두 사용해야 함

        int result = 2;
        Set<Character> set = new HashSet<>();

        for (String d : dic) {
            boolean isContain = true;

            // Set<Character> set = new HashSet<>();
            set.clear();
            for (char c : d.toCharArray()) {
                set.add(c);
            }

            for (int i = 0; i < spell.length; i++) {
                char s = spell[i].charAt(0);
                if (!set.contains(s)) isContain = false;
            }

            if (isContain) result = 1;
        }

        return result;
    }
}
