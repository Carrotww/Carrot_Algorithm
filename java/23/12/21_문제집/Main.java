// https://www.acmicpc.net/problem/1766

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        ArrayList<Integer>[] graph = new ArrayList[n+1];
        int[] indegree = new int[n+1];

        for (int i=1; i<n+1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            indegree[b]++;
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i=1; i<n+1; i++) {
            if (indegree[i] == 0) {
                pq.add(i);
            }
        }
        StringBuilder sb = new StringBuilder();
        while(!pq.isEmpty()) {
            int curNode = pq.poll();
            sb.append(curNode).append(' ');
            
            for (int i=0; i<graph[curNode].size(); i++) {
                int nextNode = graph[curNode].get(i);
                indegree[nextNode]--;
                if (indegree[nextNode] == 0) {
                    pq.add(nextNode);
                }
            }
        }
        System.out.println(sb);
    }
}
