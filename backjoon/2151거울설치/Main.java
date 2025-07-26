
import java.util.*;
import java.io.*;

class Node implements Comparable<Node> {
	int r;
	int c;
	int d;
	int cnt;

	Node (int r, int c, int d, int cnt) {
		this.r = r;
		this.c = c;
		this.d = d;
		this.cnt = cnt;
	}

	@Override
	public int compareTo(Node o) {
		return Integer.compare(this.cnt, o.cnt);
	}
}

public class Main {
	static BufferedReader br;
	static StringTokenizer st;
	static int r, c;
	static char[][] graph;
	static int[][][] visited;
	static int startR, startC;

	public static void main(String[] args) throws IOException {
		input();
		int result = dj();
		System.out.println(result);
	}

	public static int dj() {
		PriorityQueue<Node> pq = new PriorityQueue<>();

		for (int d = 0; d < 4; d++) {
			Node startNode = move(0, new Node(startR, startC, d, 0));
			if (check(startNode)) pq.add(startNode);
		}

		while (!pq.isEmpty()) {
			Node curNode = pq.poll();
			if (graph[curNode.r][curNode.c] == '#' && (curNode.r != startR || curNode.c != startC)) return curNode.cnt;

			Node nNode = move(0, curNode);
			if (!check(nNode)) continue;

			if (graph[nNode.r][nNode.c] == '!') {
				// 거울일때
				Node leftNode = move(1, nNode);
				Node rightNode = move(3, nNode);

				if (check(leftNode)) pq.add(leftNode);
				if (check(rightNode)) pq.add(rightNode);
			} else if (graph[nNode.r][nNode.c] == '*') {
				continue;
			}

			pq.add(nNode);
		}

		return -1;
	}

	public static void input() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		r = Integer.parseInt(st.nextToken());
		c = r;

		graph = new char[r][c];
		visited = new int[r][c][4];

		for (int i = 0; i < r; i++) {
			String line = br.readLine();
			for (int j = 0; j < c; j++) {
				graph[i][j] = line.charAt(j);
				if (graph[i][j] == '#') {
					startR = i;
					startC = j;
				}
			}
		}
	}

	public static boolean check(Node node) {
		if (node.r < 0 || node.r >= r || node.c < 0 || node.c >= c) return false;
		if (visited[node.r][node.c][node.d] == 1) return false;
		visited[node.r][node.c][node.d] = 1;
		return true;
	}

	public static Node move(int direct, Node node) {
		// int[] dr = new int[] {1, 1, 1, 0, -1, -1, -1, 0};
		// int[] dc = new int[] {1, 0, -1, -1, -1, 0, 1, 1};

		int[] dr = new int[] {-1, 0, 1, 0};
		int[] dc = new int[] {0, 1, 0, -1};

		// direct == 0 그대로 직진
		// direct == 2, 6 -> 거울에 팅겨서 가는 것 좌우 90도로 지정

		int nR, nC, nCnt, nD;
		if (direct == 0) {
			nR = node.r + dr[node.d];
			nC = node.c + dc[node.d];
			nCnt = node.cnt;
			nD = node.d;
		} else {
			nR = node.r;
			nC = node.c;
			nCnt = node.cnt + 1;
			nD = (direct + node.d) % 4;
		}
		
		return new Node(nR, nC, nD, nCnt);
	}
}
