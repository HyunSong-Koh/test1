#vcf 파일에서 ALT의 개수를 세어보세요. (multi alt allele에 주의)

alt_cnt = 0
with open("070.vcf",'r') as handle:
    for line in handle:
        line = line.strip()
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.split("\t")   
            # '#'으로 시작하는 header의 column을 \t 를 기준으로 split 하여 header리스트에 저장
        
        contents = line.split("\t")
        chrom = contents[0]
        pos = contents[1]
        id_ = contents[2]
        ref = contents[3]
        alts = contents[4].split(",") 
        
        for alt in alts:
            alt_cnt += 1
print(f"#alt = {alt_cnt}")
        

    
