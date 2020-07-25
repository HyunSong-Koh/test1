#059.fasta 파일의 각 염기를 파이썬 dictionary를 사용하여 세어보세요.

dic_cnt = {}
with open("059.fasta",'r') as handle:
    for line in handle:
        line = line.strip()
        if line.startswith(">"):
            continue
        for base in line:
            if base in dic_cnt:
                dic_cnt[base] += 1
            else:
                dic_cnt[base] = 1

#각 염기별 개수 출력과 전체 염기 개수 출력
total = 0
for key, value in dic_cnt.items():
    print(key, value)
    total += value
print("total base num:", total)

