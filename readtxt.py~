import sys
import json

#txt파일 읽기 함수  (read_sample.txt)
def read_txt(file_name: str) -> str:
    ret = ""
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            ret += line.strip()
    return ret


#csv파일 읽기 함수 (read_sample.cvs)
def read_csv(file_name: str) -> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(",") # header의 속성 list
                continue
            splitted = line.strip().split(",")  # header이후 line들을 ,로 구분하여 splitted 리스트에 저장.

            d = dict(zip(header, splitted)) 
            # 내장함수zip()은 동일한 개수로 이루어진 자료형을 묶어줌.
            ret.append(d)            
    return ret

"""
csv파일 format.----

#id,sequence,species
1,ACAGGGTTA,Influenza
2,TTAACCAAG,Herpes
3,GCGAATGAC,Epstein-barr

"""

#tsv파일 읽기 함수 (read_sample.tvs)
def read_tsv(file_name: str) -> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t") # header의 속성 list
                continue
            splitted = line.strip().split("\t")  # header이후 line들을 ,로 구분하여 splitted 리스트에 저장.

            d = dict(zip(header, splitted)) 
            # 내장함수zip()은 동일한 개수로 이루어진 자료형을 묶어줌.
            ret.append(d)            
    return ret


# json 포맷으로 변환 함수
def to_json(l: list, file_name: str) -> None:
    with open(file_name,'w') as handle:
        json.dump(l, handle, indent=4)

def read_json(file_name: str) -> list:
    with open(file_name,'r') as handle:
        l = json.load(handle)
    return l
# 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv[0]} [txt]")
        sys.exit()
        
    file_name = sys.argv[1]  #file_name에 실행 파일 다음의 인수가 들어감
    #txt = read_txt(file_name)
    txt = read_csv(file_name)
    #txt = read_tsv(file_name)
    #print(txt)
    to_json(txt,"read_sample.json")


