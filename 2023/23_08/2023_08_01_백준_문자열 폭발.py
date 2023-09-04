# https://www.acmicpc.net/problem/9935

# if __name__ == "__main__":
#     import sys
#     input = sys.stdin.readline

#     word = input().rstrip()
#     init_word = word
#     target = input().rstrip()

#     while True:
#         word = word.replace(target, '', 1)
#         if word == init_word:
#             break
#         init_word = word

#     if word == '':
#         print("FRULA")
#     else:
#         print(word)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    word = input().rstrip()
    target = input().rstrip()
    stack = []
    
    for i in range(len(word)):
        stack.append(word[i])
        if ''.join(stack[-len(target):]) == target:
            for _ in range(len(target)):
                stack.pop()
    
    if stack:
        print(''.join(stack))
    else:
        print()
        