import java.util.*;
import java.io.*;

public class Main {
    static int result;
    static char[][] graph;
    static int[][] visited;
    static int r, c, curR, curC, nR, nC;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    static class Node {
        int nodeR, nodeC;

        public Node(int nodeR, int nodeC) {
            this.nodeR = nodeR;
            this.nodeC = nodeC;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        graph = new char[r][c];
        for (int i = 0; i < r; i ++) {
            String t = br.readLine();
            for (int j = 0; j < c; j ++) {
                char c = t.charAt(j);
                graph[i][j] = c;
            }
        }

        for (int i = 0; i < r; i ++) {
            for (int j = 0; j < c; j ++) {
                if (graph[i][j] == 'L') bfs(i, j);
            }
        }

        System.out.println(result);
    }

    static void bfs(int inputR, int inputC) {
        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(inputR, inputC));
        visited = new int[r][c];
        for (int[] v : visited) {
            Arrays.fill(v, -1);
        }
        visited[inputR][inputC] = 0;

        while (!queue.isEmpty()) {
            Node node = queue.poll();
            curR = node.nodeR;
            curC = node.nodeC;

            for (int d = 0; d < 4; d ++) {
                nR = curR + dr[d];
                nC = curC + dc[d];

                if ((nR < 0 || nR >= r) || (nC < 0 || nC >= c)) {
                    continue;
                }
                if (visited[nR][nC] == -1 && graph[nR][nC] == 'L') {
                    visited[nR][nC] = visited[curR][curC] + 1;
                    queue.offer(new Node(nR, nC));
                    result = Math.max(result, visited[nR][nC]);
                }
            }
        }
    }
}