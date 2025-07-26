
#include <stdio.h>

int main() {
	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		int a, b;
		scanf("%d %d", &a, &b);

		if (a == b) {
			printf("%d", a * 10);
			continue;
		}

		while (a != b) {
			if (a > b)
				a /= 2;
			else
				b /= 2;

			if (a == b) {
				printf("%d\n", a * 10);
			}
				
		}
	}
}
