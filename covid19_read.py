#명령어 창에서 인수로 읽을 fasta파일명을 받음.

import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta.gz]")
    sys.exit()

f = sys.argv[1]
        
d = {}  #염기와 개수를 key:value로 담을 딕셔너리
with open(f,'r') as handle:
    for line in handle:
        line = line.strip()
        if line.startswith(">"):
            continue
        for s in line:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1

total = 0
for key, value in d.items():
    total += value
    print(f"{key}: {d[key]}")
print(f"\ntotal seq num: {total}")

"""
with open("covid_result.txt",'w') as handle:
    handle.write(f"A: {d['A']}\n")
    handle.write(f"C: {d['C']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"T: {d['T']}\n")
    handle.write(f"total seq num: {total}") # 출력안됨..?
"""
