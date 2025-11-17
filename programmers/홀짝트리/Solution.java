package 홀짝트리;

import java.util.*;

class Solution {
    public int[] solution(int[] nodes, int[][] edges) {

        int maxNode = 0;
        for (int n : nodes) maxNode = Math.max(maxNode, n);

        List<Integer>[] graph = new List[maxNode + 1];
        int[] indegree = new int[maxNode + 1];

        for (int i = 0; i < maxNode; i++) {
            graph[i] = new ArrayList<>();
        }

        int[] result = new int[2];

        for (int[] edge : edges) {
            int start = edge[0];
            int end = edge[1];

            indegree[start]++;
            indegree[end]++;

            graph[start].add(end);
            graph[end].add(start);
        }

        int[] visited = new int[maxNode + 1];

        for (int node : nodes) {
            // 홀수 1 짝수 -1
            int cnt = (indegree[node] & 1) == 0 ? -1 : 1;
            // 홀수 1 짝수 -1
            int v = (node & 1) == 0 ? -1 : 1;

            // 홀짝 = 1, 역홀짝 = -1
            int rootTree = cnt * v;

            // root는 제대로
            // 자식들은 indegree -- 해야함
            if (visited[node] == 1) continue;
            Deque<Integer> dq = new ArrayDeque<>();
            dq.add(node);
            boolean isTrue = true;

            while (!dq.isEmpty()) {
                int cur = dq.poll();
                visited[cur] = 1;

                for (int next : graph[cur]) {
                    if (visited[next] == 1) continue;

                    int nextCnt = ((indegree[next] - 1) & 1) == 0 ? -1 : 1;
                    int nextV = (next & 1) == 0 ? -1 : 1;

                    if (rootTree != (nextCnt * nextV)) isTrue = false;
                    dq.add(next);
                }
            }

            if (isTrue) {
                int idx = rootTree == 1 ? 0 : 1;
                result[idx]++;
            }
        }

        return result;
    }
}