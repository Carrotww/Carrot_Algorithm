import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) {
		int[] ary = new int[]{1, 2, 3, 4, 5, 6, 7};
		binarySearch.binarysearch(1, ary);
	}
}

class Bfs {
	public static void bfs(int start, Map<Integer, List<Integer>> graph) {
		Queue<Integer> queue = new LinkedList<>();
		Set<Integer> visited = new HashSet<>();

		queue.add(start);
		visited.add(start);

		while (!queue.isEmpty()) {
			int curNode = queue.poll();
			System.out.println("visite node : " + curNode);

			for (int nextNode : graph.getOrDefault(curNode, new ArrayList<>())) {
				if (!visited.contains(nextNode)) {
					queue.add(nextNode);
					visited.add(nextNode);
				}
			}
		}
	}
}

class Dfs {
	public static void dfsRecursion(int node, Map<Integer, List<Integer>> graph, Set<Integer> visited) {
		if (visited.contains(node)) {
			return;
		}

		visited.add(node);
		System.out.println("visite node : " + node);

		for (int nextNode : graph.getOrDefault(node, new ArrayList<>())) {
			dfsRecursion(nextNode, graph, visited);
		}
	}

	public static void dfsStack(int start, Map<Integer, List<Integer>> graph) {
		Stack<Integer> stack = new Stack<>();
		Set<Integer> visited = new HashSet<>();

		stack.push(start);

		while (!stack.isEmpty()) {
			int curNode = stack.pop();
			if (!visited.contains(curNode)) {
				visited.add(curNode);
				List<Integer> nextNodeList = graph.getOrDefault(curNode, new ArrayList<>());

				for (int i = nextNodeList.size() - 1; i > -1; i--) {
					int nextNode = nextNodeList.get(i);
					if (!visited.contains(nextNode)) {
						stack.push(nextNode);
					}
				}
			}
		}
	}
}

class Dijkstra {
	public static class Node implements Comparable<Node> {
		int vertex, cost;

		Node(int vertex, int cost) {
			this.vertex = vertex;
			this.cost = cost;
		}

		@Override
		public int compareTo(Node o) {
			return Integer.compare(this.cost, o.cost);
		}
	}

	public static Map<Integer, Integer> dijkstra(int start, Map<Integer, List<int[]>> graph) {
		Map<Integer, Integer> distance = new HashMap<>();
		PriorityQueue<Node> pq = new PriorityQueue<>();

		for (int node : graph.keySet()) {
			distance.put(node, Integer.MAX_VALUE);
		}

		distance.put(start, 0);
		pq.add(new Node(start, 0));

		while (!pq.isEmpty()) {
			Node node = pq.poll();
			int curVartex = node.vertex;
			int curCost = node.cost;

			if (curCost > distance.get(curVartex)) continue;

			for (int[] edge : graph.getOrDefault(curVartex, new ArrayList<>())) {
				int nextVartex = edge[0];
				int totalCost = curCost + edge[1];

				if (totalCost < distance.get(nextVartex)) {
					pq.add(new Node(nextVartex, totalCost));
					distance.put(nextVartex, totalCost);
				}
			}
		}

		return distance;
	}
}

class binarySearch {
	public static int binarysearch(int target, int[] ary) {
		int left = 0;
		int right = ary.length;
		System.out.println(right);

		while (left < right) {
			int mid = (left + right) / 2;
			if (ary[mid] == target) {
				return mid;
			} else if (ary[mid] < target) {
				left = mid + 1;
			} else {
				right = mid - 1;
			}
		}

		return -1;
	}

	public static int lowerbound(int target, int[] ary) {
		int left = 0;
		int right = ary.length;

		while (left < right) {
			int mid = (left + right) / 2;
			if (ary[mid] < target) {
				left = mid + 1;
			} else {
				right = mid;
			}
		}
		return right;
	}

	public static int upperbound(int target, int[] ary) {
		int left = 0;
		int right = ary.length;

		while (left < right) {
			int mid = (left + right) / 2;
			if (ary[mid] <= target) {
				left = mid + 1;
			} else {
				right = mid;
			}
		}
		return right;
	}
}















