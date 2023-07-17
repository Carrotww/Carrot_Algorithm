# https://www.acmicpc.net/problem/1744

def solve():
	import sys
	N = int(sys.stdin.readline())
	num_list = []
	mius_list = []
	zero_list = []
	result = 0
	for _ in range(N):
		num = int(sys.stdin.readline())
		if num == 0:
			zero_list.append(num)
		elif num < 0:
			mius_list.append(num)
		elif num == 1:
			result += 1
		else:
			num_list.append(num)

	num_list.sort()
	while num_list:
		total = num_list.pop()
		if num_list:
			total *= num_list.pop()
		result += total

	mius_list.sort(reverse=True)
	while len(mius_list) > 1:
		t1 = mius_list.pop()
		t2 = mius_list.pop()
		result += t1 * t2

	if len(mius_list) > len(zero_list):
		for idx in range(len(zero_list), len(mius_list)):
			result += mius_list[idx]

	print(result)

if __name__ == "__main__":
	solve()
