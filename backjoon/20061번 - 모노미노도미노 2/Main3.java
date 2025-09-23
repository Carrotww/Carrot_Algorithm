import java.io.*;
import java.util.*;

public class Main3 {
    static boolean[][] G = new boolean[6][4]; // green: rows 0..5, cols 0..3 (0..1 light, 2..5 dark)
    static boolean[][] B = new boolean[4][6]; // blue : rows 0..3, cols 0..5 (0..1 light, 2..5 dark)
    static int score = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int t = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            // 1) 초록판 낙하 (y 열 기준)
            dropGreen(t, y);

            // 2) 파란판 낙하 (x 행 기준, t 회전: 2<->3)
            int bt = (t == 2 ? 3 : (t == 3 ? 2 : 1));
            dropBlue(bt, x);

            // 3) 라인 제거
            clearGreen();
            clearBlue();

            // 4) 연한 영역 처리
            pushGreenLight();
            pushBlueLight();
        }

        // 남은 칸 수 카운트
        int remain = countGreen() + countBlue();

        // 출력: 점수, 남은 칸
        System.out.println(score);
        System.out.println(remain);
    }

    // ---------- 초록판 ----------
    static void dropGreen(int t, int y) {
        if (t == 1) { // 1x1
            int r = 0;
            while (r + 1 < 6 && !G[r + 1][y]) r++;
            G[r][y] = true;
        } else if (t == 2) { // 1x2 (가로)
            int r = 0;
            while (r + 1 < 6 && !G[r + 1][y] && !G[r + 1][y + 1]) r++;
            G[r][y] = G[r][y + 1] = true;
        } else { // t==3, 2x1 (세로)
            int r = 0;
            while (r + 2 < 6 && !G[r + 2][y]) r++;
            G[r][y] = G[r + 1][y] = true;
        }
    }

    static void clearGreen() {
        for (int r = 5; r >= 2; ) {
            boolean full = true;
            for (int c = 0; c < 4; c++) if (!G[r][c]) { full = false; break; }
            if (full) {
                score++;
                // 아래로 당기기
                for (int i = r; i > 0; i--)
                    for (int c = 0; c < 4; c++) G[i][c] = G[i - 1][c];
                for (int c = 0; c < 4; c++) G[0][c] = false;
                // 같은 r 다시 검사 (연쇄 가능)
            } else r--;
        }
    }

    static void pushGreenLight() {
        int cnt = 0;
        for (int r = 0; r <= 1; r++) {
            for (int c = 0; c < 4; c++) {
                if (G[r][c]) { cnt++; break; }
            }
        }
        while (cnt-- > 0) {
            // 전체 한 칸 아래로
            for (int r = 5; r > 0; r--)
                for (int c = 0; c < 4; c++) G[r][c] = G[r - 1][c];
            for (int c = 0; c < 4; c++) G[0][c] = false;
        }
    }

    static int countGreen() {
        int sum = 0;
        for (int r = 2; r < 6; r++)
            for (int c = 0; c < 4; c++)
                if (G[r][c]) sum++;
        return sum;
    }

    // ---------- 파란판 ----------
    static void dropBlue(int t, int x) {
        if (t == 1) { // 1x1 -> 행 x에서 오른쪽
            int col = 0;
            while (col + 1 < 6 && !B[x][col + 1]) col++;
            B[x][col] = true;
        } else if (t == 2) { // 2x1 (세로) -> 행 x, x+1 동시에 오른쪽
            int col = 0;
            while (col + 1 < 6 && !B[x][col + 1] && !B[x + 1][col + 1]) col++;
            B[x][col] = B[x + 1][col] = true;
        } else { // t==3, 1x2 (가로) -> 행 x에서 폭 2
            int col = 0;
            while (col + 2 < 6 && !B[x][col + 2]) col++;
            B[x][col] = B[x][col + 1] = true;
        }
    }

    static void clearBlue() {
        for (int c = 5; c >= 2; ) {
            boolean full = true;
            for (int r = 0; r < 4; r++) if (!B[r][c]) { full = false; break; }
            if (full) {
                score++;
                // 왼쪽으로 당기기
                for (int j = c; j > 0; j--)
                    for (int r = 0; r < 4; r++) B[r][j] = B[r][j - 1];
                for (int r = 0; r < 4; r++) B[r][0] = false;
                // 같은 c 다시 검사
            } else c--;
        }
    }

    static void pushBlueLight() {
        int cnt = 0;
        for (int c = 0; c <= 1; c++) {
            for (int r = 0; r < 4; r++) {
                if (B[r][c]) { cnt++; break; }
            }
        }
        while (cnt-- > 0) {
            // 전체 한 칸 왼쪽으로
            for (int c = 5; c > 0; c--)
                for (int r = 0; r < 4; r++) B[r][c] = B[r][c - 1];
            for (int r = 0; r < 4; r++) B[r][0] = false;
        }
    }

    static int countBlue() {
        int sum = 0;
        for (int c = 2; c < 6; c++)
            for (int r = 0; r < 4; r++)
                if (B[r][c]) sum++;
        return sum;
    }
}
