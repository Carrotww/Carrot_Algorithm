# https://www.acmicpc.net/problem/1541

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    input_val = input().strip().split('-')

    total = 0
    for val in input_val[0].split('+'):
        total += int(val)
    
    for val in input_val[1::]:
        for v in val.split('+'):
            total -= int(v)
    
    print(total)