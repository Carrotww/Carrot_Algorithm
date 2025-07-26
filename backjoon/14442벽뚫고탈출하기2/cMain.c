
#include <stdio.h>

#define MAX 1001
#define QUEUE_SIZE 10000000

typedef struct {
    int r, c, k;
} Node;

int r, c, k;
int graph[MAX][MAX];
int visited[MAX][MAX][11]; // k 최대 10
int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

Node queue[QUEUE_SIZE];
int front = 0, rear = 0;

void enqueue(Node n) {
    queue[rear++] = n;
}

Node dequeue() {
    return queue[front++];
}

int bfs() {
    enqueue((Node){0, 0, 0});
    visited[0][0][0] = 1;

    while (front < rear) {
        Node cur = dequeue();

        if (cur.r == r - 1 && cur.c == c - 1) {
            return visited[cur.r][cur.c][cur.k];
        }

        for (int d = 0; d < 4; d++) {
            int nr = cur.r + dr[d];
            int nc = cur.c + dc[d];

            if (nr < 0 || nr >= r || nc < 0 || nc >= c) continue;

            // 벽인데 아직 k 안 찼으면 부수고 이동
            if (graph[nr][nc] == 1 && cur.k < k && visited[nr][nc][cur.k + 1] == 0) {
                visited[nr][nc][cur.k + 1] = visited[cur.r][cur.c][cur.k] + 1;
                enqueue((Node){nr, nc, cur.k + 1});
            }
            // 빈칸이면 그대로 이동
            else if (graph[nr][nc] == 0 && visited[nr][nc][cur.k] == 0) {
                visited[nr][nc][cur.k] = visited[cur.r][cur.c][cur.k] + 1;
                enqueue((Node){nr, nc, cur.k});
            }
        }
    }

    return -1;
}

int main() {
    scanf("%d %d %d", &r, &c, &k);

    for (int i = 0; i < r; i++) {
        char line[MAX];
        scanf("%s", line);
        for (int j = 0; j < c; j++) {
            graph[i][j] = line[j] - '0';
        }
    }

	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			printf("%d ", graph[i][j]);
		}
		printf("\n");
	}

    int result = bfs();
    printf("%d\n", result);
    return 0;
}
