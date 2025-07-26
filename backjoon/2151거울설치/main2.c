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
char graph[MAX][MAX];
int visited[MAX][MAX][4];
int dr[4] = {-1, 0, 1, 0}; // 북 동 남 서
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

int bfs(int endR, int endC) {
    while (front < rear) {
        Node node = dequeue();

        // 거울이면 방향 바꾼 경우도 고려
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

        // 직진은 while로 쭉 가게
        int nr = node.r + dr[node.d];
        int nc = node.c + dc[node.d];
        if (check(nr, nc) && visited[nr][nc][node.d] > node.cnt) {
            visited[nr][nc][node.d] = node.cnt;
            enqueue((Node){nr, nc, node.d, node.cnt});
        }
    }

    // 도착지점 방향 중 최소값
    int result = INF;
    for (int i = 0; i < 4; i++) {
        if (visited[endR][endC][i] < result) {
            result = visited[endR][endC][i];
        }
    }
    return result;
}

int main() {
    scanf("%d", &r);
    c = r;

    int mirrorCount = 0;
    int endR = -1, endC = -1;

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
        int nr = startR + dr[i];
        int nc = startC + dc[i];
        if (check(nr, nc)) {
            visited[nr][nc][i] = 0;
            enqueue((Node){nr, nc, i, 0});
        }
    }

    int result = bfs(endR, endC);
    printf("%d\n", result);
    return 0;
}
