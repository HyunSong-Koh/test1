#vcf 파일에서 INFO 컬럼의 rs값이 있는 행의 chromosome, position, rs값, REF, ALT를 출력해보세요.

with open("070.vcf",'r') as handle:
    for line in handle:
        line = line.strip()
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.split("\t")   
            # '#'으로 시작하는 header의 column을 \t 를 기준으로 split 하여 header리스트에 저장
            print(header)
            print(f"{header[0]} \t{header[1]} \t{header[2]} \t{header[3]} \t{header[4]}")
        contents = line.split("\t")
        chrom = contents[0]
        pos = contents[1]
        id_ = contents[2]
        ref = contents[3]
        alt = contents[4]
        if id_.startswith("rs"):
            print(f"{chrom} \t{pos} \t{id_} \t{ref} \t{alt}")

        

    
