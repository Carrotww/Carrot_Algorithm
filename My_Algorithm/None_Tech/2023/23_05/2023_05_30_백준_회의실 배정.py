# https://www.acmicpc.net/workbook/view/7320

def solve1():
	import sys
	N = int(sys.stdin.readline())
	meet = []
	for _ in range(N):
		start, end = map(int, sys.stdin.readline().split())
		meet.append([start, end])

	meet.sort(key=lambda x:x[0])
	result = 0
	for idx in range(N):
		cnt = 1
		end_time = meet[idx][1]
		for n_idx in range(idx+1, N):
			if meet[n_idx][0] < end_time:
				continue
			else:
				end_time = meet[n_idx][1]
				cnt += 1
		result = max(result, cnt)

	print(result)

def solve():
	import sys
	N = int(sys.stdin.readline())
	meet = []
	for _ in range(N):
		start, end = map(int, sys.stdin.readline().split())
		meet.append([start, end])

	meet.sort(key=lambda x:(x[1], x[0]))
	result = 1
	end_time = meet[0][1]

	for idx in range(1, N):
		if meet[idx][0] < end_time:
			continue
		else:
			end_time = meet[idx][1]
			result += 1

	print(result)

if __name__ == "__main__":
	solve()