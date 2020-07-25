import json

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


# 딕셔너리 결과를 json파일로 저장.(hw3-2.json)
with open("hw3-2.json",'w') as handle:
    json.dump(dic_cnt, handle, indent=4)
