package 홀짝트리;

import java.util.*;

class Solution {
    public int[] solution(int[] nodes, int[][] edges) {
        int[] result = new int[2];

        int maxNode = 0;
        for (int node : nodes) { maxNode = Math.max(maxNode, node); }
        List<Integer>[] graph = new ArrayList[maxNode + 1];

        for (int node : nodes) {
            graph[node] = new ArrayList<>();
        }
        int[] indegree = new int[maxNode + 1];

        for (int[] edge : edges) {
            int a = edge[0];
            int b = edge[1];
            graph[a].add(b);
            graph[b].add(a);
            indegree[a]++;
            indegree[b]++;
        }

        int[] visited = new int[maxNode + 1];

        // node를 순회하면서 홀수인지 짝수인지 역홀수인지 역짝수인지 변수 선언 후 ++
        for (int node : nodes) {
            int oddTree = 0;
            int evenTree = 0;
            int reverseOddTree = 0;
            int reverseEvenTree = 0;

            if (visited[node] == 1) continue;

            visited[node] = 1;

            ArrayDeque<Integer> dq = new ArrayDeque<>();
            dq.add(node);

            while (!dq.isEmpty()) {
                int cur = dq.poll();

                int childCnt = indegree[cur];
                
                if (childCnt % 2 == 0 && cur % 2 == 0) {
                    evenTree++;
                } else if (childCnt % 2 == 0 && cur % 2 == 1) {
                    reverseOddTree++;
                } else if (childCnt % 2 == 1 && cur % 2 == 0) {
                    reverseEvenTree++;
                } else {
                    oddTree++;
                }

                for (int next : graph[cur]) {
                    if (visited[next] == 1) continue;
                    visited[next] = 1;

                    dq.add(next);
                }
            }

            if (oddTree + evenTree == 1) {
                result[0]++;
            }
            
            if (reverseOddTree + reverseEvenTree == 1) {
                result[1]++;
            }
        }

        return result;
    }
}