import java.io.*;
import java.util.*;

public class Main {
    static int n, m, r;
    static int[] visited;
    static ArrayList<Integer>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n + 1];

        for (int i = 0; i <= n; i ++) {
            graph[i] = new ArrayList<Integer>();
        }

        for (int i = 0; i < m; i ++) {
            int start, end;
            st = new StringTokenizer(br.readLine());
            start = Integer.parseInt(st.nextToken());
            end = Integer.parseInt(st.nextToken());

            graph[start].add(end);
            graph[end].add(start);
        }

        for (int i = 0; i <= n; i ++) {
            if (graph[i] != null && !graph[i].isEmpty()) {
                Collections.sort(graph[i]);
            }
        }
        visited = new int[n+1];

        bfs(r);

        for (int i = 1; i <= n; i ++) {
            System.out.println(visited[i]);
        }
    }

    static void bfs(int node) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(node);
        visited[node] = 1;
        int cnt = 1;
        int curNode;

        while (!queue.isEmpty()) {
            curNode = queue.poll();

            for (int nNode : graph[curNode]) {
                if (visited[nNode] == 0) {
                    cnt ++;
                    visited[nNode] = cnt;
                    queue.add(nNode);
                }
            }
        }
    }
}