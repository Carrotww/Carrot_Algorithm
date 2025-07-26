// 메모리 초과

import java.io.*;
import java.util.*;

public class _14442 {
    private static int[] dx = {0, 1, 0, -1};
    private static int[] dy = {1, 0, -1, 0};
    private static int N;
    private static int M;
    private static int K;
    private static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        board = new int[N][M];

        for (int i = 0; i < N; i++) {
            String temp = br.readLine();
            for (int j = 0; j < M; j++) {
                board[i][j] = Character.getNumericValue(temp.charAt(j));
            }
        }

        int answer = bfs(0, 0);
        System.out.println(answer);

        br.close();
    }

    private static int bfs(int startX, int startY) {
        Deque<int[]> queue = new ArrayDeque<>();
        int[][][] visited = new int[N][M][K + 1];

        queue.offerLast(new int[]{startX, startY, 0});
        visited[startX][startY][0] = 1;

        while (!queue.isEmpty()) {
            int[] temp = queue.pollFirst();
            int x = temp[0];
            int y = temp[1];
            int z = temp[2];

            if (x == N - 1 && y == M - 1) {
                return visited[x][y][z];
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx < 0 || nx > N - 1 || ny < 0 || ny > M - 1) {
                    continue;
                }

                if (board[nx][ny] == 0) {
                    queue.offerLast(new int[]{nx, ny, z});
                    visited[nx][ny][z] = visited[x][y][z] + 1;
                } else if (z < K) {
                    queue.offerLast(new int[]{nx, ny, z + 1});
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1;
                }
            }
        }

        return -1;
    }
}

