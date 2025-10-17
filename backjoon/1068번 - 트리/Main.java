/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1068                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1068                           #+#        #+#      #+#    */
/*   Solved: 2025/10/17 11:07:47 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        List<List<Integer>> graph = new ArrayList<>(N);
        for (int i = 0; i < N; i++)
            graph.add(new ArrayList<>());

        // indegree index : node, value : indegree cnt
        int[] indegree = new int[N];
        // find parent - index : child val : parent
        int[] findParent = new int[N];
        Arrays.fill(findParent, -1);
        int root = -1;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int child = i;
            int parent = Integer.parseInt(st.nextToken());
            if (parent == -1) {
                root = i;
                continue;
            }

            // parent -> child
            graph.get(parent).add(child);
            // 부모 저장
            findParent[child] = parent;
            indegree[parent]++;
        }

        st = new StringTokenizer(br.readLine());
        int deleteNode = Integer.parseInt(st.nextToken());
        if (deleteNode == root) {
            System.out.println(0);
            return;
        }
        Deque<Integer> dq = new ArrayDeque<>();
        dq.add(deleteNode);

        while (!dq.isEmpty()) {
            int curNode = dq.poll();

            indegree[curNode] = -1;
            int parent = findParent[curNode];
            indegree[parent]--;

            for (int child : graph.get(curNode)) {
                dq.add(child);
            }
        }

        int result = 0;
        for (int node : indegree) {
            if (node == 0)
                result++;
        }

        System.out.println(result);
    }
}