
#include <stdio.h>

#define MAX 1001

int r, c, k;
int graph[MAX][MAX];
int visited[MAX][MAX][11];
int dr[4] = {1, -1, 0, 0};
int dc[4] = {0, 0, 1, -1};

typedef struct {
	int r, c, k;
} Node;

Node queue[10000000];

void enqueue(Node *q, Node n, int *rear) {
    q[(*rear)++] = n;
}

Node dequeue(Node *q, int *front) {
	return q[(*front)++];
}

int bfs() {
	int front = 0;
	int rear = 0;

	enqueue(queue, (Node) {0, 0, 0}, &rear);

	visited[0][0][0] = 1;
	while (front < rear) {
		Node cur = dequeue(queue, &front);

		if (cur.r == r - 1 && cur.c == c - 1) {
			return visited[cur.r][cur.c][cur.k];
		}

		for (int d = 0; d < 4; d++) {
			int nR = dr[d] + cur.r;
			int nC = dc[d] + cur.c;

			if (nR < 0 || nR >= r || nC < 0 || nC >= c) continue;

			if (graph[nR][nC] == 1 && cur.k < k && visited[nR][nC][cur.k + 1] == 0) {
				visited[nR][nC][cur.k + 1] = visited[cur.r][cur.c][cur.k] + 1;
				enqueue(queue, (Node) {nR, nC, cur.k + 1}, &rear);
			} else if (graph[nR][nC] == 0 && visited[nR][nC][cur.k] == 0) {
				visited[nR][nC][cur.k] = visited[cur.r][cur.c][cur.k] + 1;
				enqueue(queue, (Node) {nR, nC, cur.k}, &rear);
			}
		}
	}

	return -1;
}

int main() {
	scanf("%d %d %d", &r, &c, &k);

	for (int i = 0; i < r; i++) {
		char input[MAX];
		scanf("%s", input);

		for (int j = 0; j < c; j++) {
			graph[i][j] = input[j] - '0';
		}
	}

	int result = bfs();
	printf("%d\n", result);
}
