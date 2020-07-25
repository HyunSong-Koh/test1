dic = {} # name과 실수를 key와 value로 받을 딕셔너리 선언
with open("data.txt",'r') as handle:
    for line in handle:
        line = line.strip()
        content = line.split()
        name = content[0]
        val = float(content[1])
        dic[name] = val
sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for key,value in sorted_dic:
    print(f"{key}\t{value}")
