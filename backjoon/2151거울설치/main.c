// bfs로 풀어보기

#include <stdio.h>

#define MAX 51
#define INF 5000

typedef struct {
	int r;
	int c;
	int d;
	int cnt;
} Node;

int r, c;
int startR, startC;
int endR, endC;
char graph[MAX][MAX];
int visited[MAX][MAX][4];
int dr[4] = {-1, 0, 1, 0};
int dc[4] = {0, 1, 0, -1};
Node queue[1000000];
int front = 0;
int rear = 0;

void enqueue(Node node) {
	queue[rear++] = node;
}

Node dequeue() {
	return queue[front++];
}

int check(int r, int c) {
    return (r >= 0 && r < MAX && c >= 0 && c < MAX && graph[r][c] != '*');
}
// int check(int curR, int curC) {
	// if (curR < 0 || curR >= r || curC < 0 || curC >= c) return 0;
	// if (graph[curR][curC] == '*') return 0;
	// return 1;
// }

int bfs() {
	while (front < rear) {
		Node node = dequeue();

		// 현 자리가 거울일 경우
		// if (graph[node.r][node.c] == '!') {
			// Node leftNode = {node.r + dr[(node.d + 1) % 4], node.c + dc[(node.d + 1) % 4], (node.d + 1) % 4, node.cnt + 1};
			// Node rightNode = {node.r + dr[(node.d + 3) % 4], node.c + dc[(node.d + 3) % 4], (node.d + 3) % 4, node.cnt + 1};

			// if (check(leftNode.r, leftNode.c) && visited[leftNode.r][leftNode.c][leftNode.d] > node.cnt + 1) {
				// visited[leftNode.r][leftNode.c][leftNode.d] = node.cnt + 1;
				// enqueue(leftNode);
			// }
			// if (check(rightNode.r, rightNode.c) && visited[rightNode.r][rightNode.c][rightNode.d] > node.cnt + 1) {
				// visited[rightNode.r][rightNode.c][rightNode.d] = node.cnt + 1;
				// enqueue(rightNode);
			// }
		// } else if (graph[node.r][node.c] == '*') {
			// continue;
		// }
        if (graph[node.r][node.c] == '!') {
            for (int turn = -1; turn <= 1; turn += 2) {
                int nd = (node.d + turn + 4) % 4;
                int nr = node.r + dr[nd];
                int nc = node.c + dc[nd];
                if (check(nr, nc) && visited[nr][nc][nd] > node.cnt + 1) {
                    visited[nr][nc][nd] = node.cnt + 1;
                    enqueue((Node){nr, nc, nd, node.cnt + 1});
                }
            }
        }

		int nR = node.r + dr[node.d];
		int nC = node.c + dc[node.d];
		if (check(nR, nC) && visited[nR][nC][node.c] > node.cnt) {
			visited[nR][nC][node.d] = node.cnt;
			enqueue((Node) {nR, nC, node.d, node.cnt});
		}
	}

	int result = INF;
	for (int i = 0; i < 4; i++) {
		if (result > visited[endR][endC][i]) {
			result = visited[endR][endC][i];
		}
	}

	return result;
}

int main() {
	scanf("%d", &r);
	c = r;
	getchar();

	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < MAX; j++) {
			graph[i][j] = '*';
		}
	}

	for (int i = 0; i < r; i++) {
		char buf[MAX];
		fgets(buf, MAX, stdin);
		for (int j = 0; buf[j] != '\n' && buf[j] != '\0'; j++) {
			graph[i][j] = buf[j];
		}
	}

	int mirrorcnt = 0;

	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (graph[i][j] == '#') {
				if (mirrorcnt == 0) {
					startR = i;
					startC = j;
				} else {
					endR = i;
					endC = j;
				}
			}
			for (int k = 0; k < 4; k++) {
				visited[i][j][k] = INF;
			}
		}
	}

	// startR,C 기준으로 해서 갈 수 있는 곳은 queue에 넣어주자
    for (int i = 0; i < 4; i++) {
        int nr = startR + dr[i];
        int nc = startC + dc[i];
        if (check(nr, nc)) {
            visited[nr][nc][i] = 0;
            enqueue((Node){nr, nc, i, 0});
        }
    }

	int result = bfs();
	printf("%d\n", result);
}

