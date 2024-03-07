# https://www.acmicpc.net/problem/11497

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        ary = list(map(int, input().split()))

        ary.sort(reverse=True)
        n_ary = [0] * n
        left_idx, right_idx = 0, n-1
        cur_direct = 0
        for i in range(n):
            if cur_direct == 0:
                n_ary[left_idx] = ary[i]
                cur_direct = 1
                left_idx += 1
            else:
                n_ary[right_idx] = ary[i]
                cur_direct = 0
                right_idx -= 1
        max_val = 0
        for i in range(n-1):
            max_val = max(abs(n_ary[i+1]-n_ary[i]), max_val)
        max_val = max(abs(n_ary[-1]-n_ary[0]), max_val)
        result.append(max_val)

    for r in result:
        print(r)
        

