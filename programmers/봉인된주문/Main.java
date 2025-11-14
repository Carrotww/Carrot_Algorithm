
import java.util.*;
import java.io.*;

class Solution {
    public String solution(long target, String[] bans) {
        String answer = "";
        int n = bans.length;
        long[] bansLong = new long[n];
        
        for (int i = 0; i < n; i++) {
            bansLong[i] = stringToLong(bans[i]);
        }
        
        int left = 0;
        int right = n;
        
        // target이 제일 크면
        if (target >= bansLong[n]) {
            return longToString(target);
        }
        
        while (left < right) {
            int mid = left + (right - left) / 2;

            if (bansLong[mid] < target) {
                target += left;
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        return answer;
    }
    
    public long stringToLong(String str) {
        // "aab" -> long
        long result = 0;
        int n = str.length();

        for (int i = 0; i < n; i++) {
            char cur = str.charAt(i);
            int digit = cur - 'a' + 1;
            result = result * 26 + digit;
        }

        return result;
    }
    
    public String longToString(long l) {
        StringBuilder sb = new StringBuilder();

        while (l > 26) {
            long mod = l % 26;
            l /= 26;
            char c = (char) ('a' - mod);

            sb.append(c);

        }

        sb.append((l % 26) + 'a');

        return sb.reverse().toString();
    }
}