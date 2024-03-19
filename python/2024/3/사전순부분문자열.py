# https://github.com/wooks527/programming/blob/master/programmers/ds/stack/alphabetical_part_string.ipynb

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    word = input().rstrip()
    stack = []
    for w in word:
        while stack and stack[-1] < w:
            stack.pop()
        stack.append(w)
    print(''.join(stack))

