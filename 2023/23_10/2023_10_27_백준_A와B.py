# https://www.acmicpc.net/problem/12904

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    s = list(input().rstrip())
    t = list(input().rstrip())
    s_len = len(s)

    while len(t) > s_len:
        if t[-1] == 'A':
            t.pop()
        else:
            t.pop()
            t = t[::-1]
    if s == t:
        print(1)
    else:
        print(0)