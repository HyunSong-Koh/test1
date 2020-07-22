"""
with open("read_sample.txt", 'r') as f:
    for line in f:
        if line.startswith(">"):
            continue
        print(line.strip(),end='')
    print()
"""

import sys

def read_txt(file_name: str) -> str:
    ret = ""
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            ret += line.strip()
    return ret


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv[0]} [txt]")
        sys.exit()
        
    file_name = sys.argv[1]  #file_name에 실행 파일 다음의 인수가 들어감
    txt = read_txt(file_name)
    print(txt)
    
