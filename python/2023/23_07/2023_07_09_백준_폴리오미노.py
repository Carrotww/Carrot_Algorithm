# https://www.acmicpc.net/submit/1343/63113754

import sys

# AAAA, BB
input = sys.stdin.readline

fill = input()
idx = 0
word = ''
result = ''


def push_result(word):
    global result

    word_len = len(word)
    if word_len % 2 == 0:
        cnt = word_len // 4
        word_len -= cnt * 4
        result += 'A' * cnt * 4
        
        cnt = word_len // 2
        result += 'B' * cnt * 2
    else:
        result = -1


while idx < len(fill) - 1:
    if fill[idx] == '.':
        push_result(word)
        word = ''
        if result == -1:
            break
        result += '.'
    else:
        word += 'X'

    idx += 1

if word and result != -1:
    push_result(word)

print(result)
