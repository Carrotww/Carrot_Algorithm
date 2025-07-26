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

int check(int curR, int curC) {
	if (curR < 0 || curR >= r || curC < 0 || curC >= c) return 0;
	if (graph[curR][curC] == '*') return 0;
	return 1;
}

int bfs() {
	while (front < rear) {
		Node node = dequeue();

		// 현 자리가 거울일 경우
		if (graph[node.r][node.c] == '!') {
			Node leftNode = {node.r + dr[(node.d + 1) % 4], node.c + dc[(node.d + 1) % 4], (node.d + 1) % 4, node.cnt + 1};
			Node rightNode = {node.r + dr[(node.d + 3) % 4], node.c + dc[(node.d + 3) % 4], (node.d + 3) % 4, node.cnt + 1};

			if (check(leftNode.r, leftNode.c) && visited[leftNode.r][leftNode.c][leftNode.d] > node.cnt + 1) {
				visited[leftNode.r][leftNode.c][leftNode.d] = node.cnt + 1;
				enqueue(leftNode);
			}
			if (check(rightNode.r, rightNode.c) && visited[rightNode.r][rightNode.c][rightNode.d] > node.cnt + 1) {
				visited[rightNode.r][rightNode.c][rightNode.d] = node.cnt + 1;
				enqueue(rightNode);
			}
		} else if (graph[node.r][node.c] == '*') {
			continue;
		}

		int nR = node.r + dr[node.d];
		int nC = node.c + dc[node.d];
		if (check(nR, nC) && visited[nR][nC][node.d] > node.cnt) {
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

    int mirrorCount = 0;

    for (int i = 0; i < r; i++) {
        scanf("%s", graph[i]);
        for (int j = 0; j < c; j++) {
            if (graph[i][j] == '#') {
                if (mirrorCount == 0) {
                    startR = i;
                    startC = j;
                    mirrorCount++;
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

    // 4방향으로 초기 큐 삽입
    for (int i = 0; i < 4; i++) {
		visited[startR][startC][i] = 0;
		enqueue((Node){startR, startC, i, 0});
    }

    int result = bfs();
    printf("%d\n", result);
    return 0;
}
