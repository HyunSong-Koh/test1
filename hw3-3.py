#059.fasta 파일의 역상보서열을 출력하는 프로그램을 작성해보세요.


dic = {}
with open("059.fasta",'r') as handle:
    for line in handle:
        line = line.strip()
        if line.startswith(">"):
            header = line   # >로 시작하는 라인은 header변수에
            continue
        if header in dic:
            dic[header] += line
        else:
            dic[header] = line
#fasta파일에서 id와 seq를 딕셔너리에 저장하였음.


#id와 역상보서열을 딕셔너리에 저장.
dic_rev_comp = {}
d_comp = {"A":"T","T":"A","G":"C","C":"G"}
for key,value in dic.items():
    rev_val = value[::-1]
    comp_val = ''
    for base in rev_val:#rev_val의 서열을 거꾸로 comp_val에 저장.               
        comp_val += d_comp[base]
    dic_rev_comp[key] = comp_val

print(dic_rev_comp) #역상보서열 출력
