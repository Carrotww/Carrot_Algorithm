
import sys
input = sys.stdin.readline

n = int(input())

score = [10 ** x for x in range(1, 11)]
alpalist = []
alpascore = {}
for _ in range(n):
    alpalist.append(input().split())

for word in alpalist:
    for w, s in zip(reversed(word[0]), score):
        if w in alpascore:
            alpascore[w] += s
        else:
            alpascore[w] = s

alparank = [(a, b) for a, b in alpascore.items()]
alparank.sort(key=lambda x:x[1], reverse=True)
val = 9
for a, s in alparank:
    alpascore[a] = val
    val -= 1

result = 0
for word in alpalist:
    temp = ''
    for w in word[0]:
        temp += str(alpascore[w])
    result += int(temp)
print(result)