import sys
import json

def read_csv(file_name):
    ret = []
    cnt = 0 #line counter
    with open(file_name,'r') as handle:
        for line in handle:
            if cnt % 2 == 0:
                header = line.strip().split(",")
                cnt += 1
                continue
            splitted = line.strip().split(",")
            
            for i in range(len(splitted)):  #숫자를 실수 type으로 바꿔저장.
                splitted[i] = float(splitted[i])
 
            d = dict(zip(header, splitted))
            ret.append(d)
            cnt += 1
    return ret


def to_json(l, file_name):
    with open(file_name,'w') as handle:
        json.dump(l, handle, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv[0]} [txt]")
        sys.exit()

    file_name = sys.argv[1]
    txt = read_csv(file_name)
    to_json(txt,"hw2.json")


