import sys
import gzip

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta.gz]")
    sys.exit()

f = sys.argv[1]

with gzip.open(f, 'rb') as handle:
    for line in handle:
        line = line.decode("utf-8")
        print(type(line.strip()))
        sys.exit()

d = {}  #염기와 개수를 key:value로 담을 딕셔너리

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


with open("result1.txt",'w') as handle:
    handle.write(f"A: {d['A']}\n")
    handle.write(f"C: {d['C']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"T: {d['T']}\n")
    handle.write(f"total seq num: {total}") # 출력안됨..?

