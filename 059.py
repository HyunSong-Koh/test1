
with open("059.fasta", 'r') as f:
    d_cnt = {}
    for line in f:
        if line.startswith(">"):
            continue
        for c in line:
            if c in d_cnt:
                d_cnt[c] += 1
            else:
                d_cnt[c] = 1
print(d_cnt)
