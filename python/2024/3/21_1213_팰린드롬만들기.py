# https://www.acmicpc.net/problem/1213

if __name__ == "__main__":
    import sys

    name = input().rstrip()

    if len(name) == 1:
        print(name)
        exit(0)

    alpa_dict = {}
    check = 0

    for n in name:
        if n in alpa_dict:
            alpa_dict[n] += 1
            check += 1
        else:
            alpa_dict[n] = 1

    can_palin = True
    result = ''
    cnt = 0
    od = ''
    for alpa, n in alpa_dict.items():
        if n % 2:
            cnt += 1
            od = alpa
            if cnt > 1:
                can_palin = False
                break

    if len(name) % 2:
        if can_palin and cnt == 1:
            for alpa in sorted(alpa_dict.keys()):
                if alpa == od:
                    result += (od * (alpa_dict[od] // 2))
                    continue
                result += (alpa * (alpa_dict[alpa] // 2))
            reverse_result = result[::-1]
            result += od
            result += reverse_result
    else:
        for alpa in sorted(alpa_dict.keys()):
            result += (alpa * (alpa_dict[alpa] // 2))
        result += result[::-1]

    if not can_palin or not check:
        print("I'm Sorry Hansoo")
    else:
        print(result)





