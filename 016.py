import sys

f = sys.argv[1]
d = {}

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line.strip():
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
print(d)

total = 0
for key,value in d.items():
    total += v
print("total seq num:", total)
