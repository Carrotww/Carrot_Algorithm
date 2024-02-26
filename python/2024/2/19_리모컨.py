# https://www.acmicpc.net/problem/1107

def dfs(target_len: int, total_num: str):
    global result
    if len(total_num) == target_len:
        result = min(result, abs(int(total_num) - int(target)) + len(total_num))
        return
    for i in range(len(available_num)):
        dfs(target_len, total_num+available_num[i])

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    start = "100"
    target = input().rstrip()
    non_btn_cnt = int(input())
    if non_btn_cnt == 0:
        button = []
    else:
        button = input().split()

    # 방향키로 처음부터 이동 가능한 경우
    need_num = abs(int(target) - int(start))
    result = need_num

    available_num = [str(i) for i in range(10) if str(i) not in button]

    total_num_set = set()
    check = {len(target), len(target)+1}
    if len(target) > 1:
        check.add(len(target) - 1)

    if not available_num:
        print(result)
    else:
        for i in check:
            dfs(i, "")
        print(result)

