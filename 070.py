"""
cnt = 0
with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        cnt += 1
print(cnt)
"""

"""
cnt = 0        
with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        splitted = line.strip().split("\t")
        if splitted[6] == "PASS":
            cnt += 1
print(cnt)
"""


"""
cnt = 0        
with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.strip().split("\t")
            filt_idx = header.index("FILTER")

        splitted = line.strip().split("\t")
        if splitted[6] == "PASS":
            cnt += 1
print(cnt)
"""

"""
with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.strip().split("\t")
            id_idx = header.index("ID")

        splitted = line.strip().split("\t")
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
        alt = splitted[4]
        if splitted[id_idx] != ".":
            print(f"{chrom}-{pos}-{alt}-{id_}")
"""

"""
cnt = 0
with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.strip().split("\t")
        splitted = line.strip().split("\t")
        alts = splitted[4].split(",")
        for alt in alts:
            cnt += 1
print(cnt)
"""


#vcf파일에서 SNP와 Insertion, Deletion의 개수 세기.

import pandas as pd
from matplotlib import pyplot as plt

d = {"snp":0,"ins":0,"del":0}
cnt = 0
with open("070.vcf", 'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.strip().split("\t")
            continue
        splitted = line.strip().split("\t")
        
        ref = splitted[3]
        alts = splitted[4].split(",")
        for alt in alts:
            if len(ref) == len(alt):
                d["snp"] += 1
            elif len(ref) > len(alt):
                d["del"] += 1
            elif len(ref) < len(alt):
                d["ins"] += 1
            else: #방어적 코딩
                raise

print(d)
df = pd.DataFrame([d])
print(df)
df.plot.bar()
plt.savefig("v.png")



