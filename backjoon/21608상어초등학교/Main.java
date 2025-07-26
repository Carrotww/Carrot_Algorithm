
import java.util.*;
import java.io.*;

public class Main {

	static BufferedReader br;
	static StringTokenizer st;
	static int n;
	static int[][] graph;
	static List<Map.Entry<Integer, HashSet<Integer>>> list;
	static int result;
	static HashMap<Integer, HashSet<Integer>> check;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		graph = new int[n][n];
		list = new ArrayList<>();
		list.add(new AbstractMap.SimpleEntry<>(0, new HashSet<>(List.of(0, 0))));
		check = new HashMap<>();

		for (int i = 0; i < n * n; i++) {
			st = new StringTokenizer(br.readLine());
			
			int curN = Integer.parseInt(st.nextToken());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());

			check.put(curN, new HashSet<>(List.of(a, b, c, d)));
			list.add(new AbstractMap.SimpleEntry<>(curN, new HashSet<>(List.of(a, b, c, d))));
		}

		int[] dr = new int[] {1, -1, 0, 0};
		int[] dc = new int[] {0, 0, 1, -1};

		for (int i = 1; i < n * n + 1; i++) {
			Map.Entry<Integer, HashSet<Integer>> map = list.get(i);
			int curN = map.getKey();
			HashSet<Integer> set = map.getValue();

			// 첫번째 조건
			// 주변 확인해서 좋아하는 애 넣기
			// 좋아하는 애 있던 없든 다 넣는데 heap으로 넣고 0 번째가 가장 많은거니까 그걸로 판별

			PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
				if (a[0] != b[0]) return b[0] - a[0];
				if (a[1] != b[1]) return a[1] - b[1];
				return a[2] - b[2];
			});

			for (int r = 0; r < n; r++) {
				for (int c = 0; c < n; c++) {
					if (graph[r][c] == 0) {
						// 조건 실행 비어있는칸 다 넣기
						int cnt = 0;

						for (int d = 0; d < 4; d++) {
							int nR = r + dr[d];
							int nC = c + dc[d];

							if (nR < 0 || nR >= n || nC < 0 || nC >= n) {
								continue;
							}

							if (set.contains(graph[nR][nC])) {
								cnt++;
							}
						}

						pq.add(new int[] {cnt, r, c});
					}
				}
			}

			int maxCnt = pq.peek()[0];
			PriorityQueue<int[]> pq2 = new PriorityQueue<>((a, b) -> {
				if (a[0] != b[0]) return b[0] - a[0];
				if (a[1] != b[1]) return a[1] - b[1];
				return a[2] - b[2];
			});

			while (!pq.isEmpty()) {
				if (pq.peek()[0] == maxCnt) {
					pq2.add(pq.poll());
				} else {
					pq.poll();
				}
			}

			if (pq2.size() == 1) {
				int t[] = pq2.poll();
				graph[t[1]][t[2]] = curN;
				continue;
			}

			PriorityQueue<int[]> pq3 = new PriorityQueue<>((a, b) -> {
				if (a[0] != b[0]) return b[0] - a[0];
				if (a[1] != b[1]) return a[1] - b[1];
				return a[2] - b[2];
			});

			while (!pq2.isEmpty()) {
				int[] t = pq2.poll();
				int r = t[1];
				int c = t[2];
				int cnt = 0;

				for (int d = 0; d < 4; d++) {
					int nR = r + dr[d];
					int nC = c + dc[d];

					if (nR < 0 || nR >= n || nC < 0 || nC >= n) {
						continue;
					}

					if (graph[nR][nC] == 0) {
						cnt++;
					}
				}
				pq3.add(new int[] {cnt, r, c});
			}

			int t[] = pq3.poll();
			graph[t[1]][t[2]] = curN;

			// ary에 heap 0번째 넣어주기 최대힙으로 해서 like, r, c 이렇게 넣자
			// 첫번째 like 기준으로 정해서 그 아래는 다 없애고 두번째 조건 실행

			// 두번째조건
			// 또 인접한 칸을 확인하면서 비어있는 칸 개수 넣어줌 이것도 그냥 heap으로 하면 될듯

			// 세번째 조건
			// heap으로 정렬할때 like, r, c like만 최대힙 나머지는 최소 힙 기준으로 했으니 그냥 하나 빼서 바로 graph에 자리 넣기
		}

		for (int r = 0; r < n; r++) {
			for (int c = 0; c < n; c++) {
				int cnt = 0;

				for (int d = 0; d < 4; d++) {
					int nR = r + dr[d];
					int nC = c + dc[d];

					if (nR < 0 || nR >= n || nC < 0 || nC >= n) {
						continue;
					}

					if (check.get(graph[r][c]).contains(graph[nR][nC])) {
						cnt++;
					}
				}

				if (cnt >= 1) result += (int) Math.pow(10, cnt - 1);
			}
		}

		System.out.println(result);
	}
}
