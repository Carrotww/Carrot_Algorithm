# https://www.acmicpc.net/problem/1789

if __name__ == "__main__":
    import sys
    
    num = int(sys.stdin.readline())

    result = 0
    i = 0
    while num >= result:
        i += 1
        result += i
    print(i-1)