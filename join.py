dic = {} # name과 실수를 key와 value로 받을 딕셔너리 선언
with open("data.txt",'r') as handle:
    for line in handle:
        line = line.strip()
        content = line.split()
        name = content[0]
        val = float(content[1])
        dic[name] = val

with open("gene.txt",'r') as handle:
    gene_list = []  # gene이름을 원소로 받을 리스트 초기화
    for line in handle:
        line = line.strip()
        gene_list.append(line) # gene이름을 리스트에 추가

dic_join = {}
for elem in gene_list:
    if elem in dic:
        dic_join[elem] = dic[elem]
    else:
        dic_join[elem] = 'NULL'

for key, value in dic_join.items():
    print(f"{key}\t{value}")

