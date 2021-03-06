"""
import sys
import gzip

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta.gz]")
    sys.exit()

f = sys.argv[1]

with gzip.open(f,'rb') as handle:
    for line in handle:
        line = line.decode("utf-8")
        print(type(line.strip()))
        sys.exit()

        
d = {}  #염기와 개수를 key:value로 담을 딕셔너리
#gzip파일을 열어, 각 염기와 그 개수를 딕셔너리 d에 저장.
with gzip.open(f,'rb') as handle:
    for line in handle:
        line = line.decode("utf-8").strip()
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


with open("result11.txt",'w') as handle:
    handle.write(f"A: {d['A']}\n")
    handle.write(f"C: {d['C']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"T: {d['T']}\n")
    handle.write(f"total seq num: {total}") # 출력안됨..?
"""


import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta.gz]")
    sys.exit()

f = sys.argv[1]
"""
with open(f,'r') as handle:
    for line in handle:
        line = line.decode("utf-8")
        print(type(line.strip()))
        sys.exit()
"""
        
d = {}  #염기와 개수를 key:value로 담을 딕셔너리
#gzip파일을 열어, 각 염기와 그 개수를 딕셔너리 d에 저장.
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


with open("covid_result.txt",'w') as handle:
    handle.write(f"A: {d['A']}\n")
    handle.write(f"C: {d['C']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"T: {d['T']}\n")
    handle.write(f"total seq num: {total}")

