// https://www.acmicpc.net/problem/3896

import java.util.*;
import java.io.*;
import java.lang.Math;

public class Main {
    static List<Integer> result;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        result = new ArrayList<>();

        for (int i = 0; i < t; i++) {
            int curNum = Integer.parseInt(br.readLine());
            result.add(solution(curNum));
        }

        for (int num : result) {
            System.out.println(num);
        }
    }

    public static int solution(int num) {
        if (findDecimal(num)) {
            return 0;
        }
        int minValue = num - 1;
        int maxValue = num + 1;

        while (!findDecimal(minValue)) {
            minValue--;
        }

        while (!findDecimal(maxValue)) {
            maxValue++;
        }

        return maxValue - minValue;
    }

    public static boolean findDecimal(int num) {
        if (num == 1 || num == 2) {
            return true;
        } else {
            for (int i = 2; i <= (int)Math.sqrt(num) + 1; i++) {
                if (num % i == 0) {
                    return false;
                }
            }
        }

        return true;
    }
}

