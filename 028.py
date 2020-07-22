import sys
#방법1 
def comp1(seq: str) -> str:
    comp = ""
    for s in seq:  # seq로 들어온 서열을 첫 문자부터 상보적인 문자를 comp에 저장
        if s == "A":
            comp += "T"
        elif s == "C":
            comp += "G"
        elif s == "G":
            comp += "C"
        elif s == "T":
            comp += "A"
    return comp

#방법2
def comp2(seq: str) -> str:
    d_comp = {"A":"T", "T":"A", "G":"C", "C":"G"}
    comp = ""
    for s in seq:
        comp += d_comp[s]
    return comp



#파이썬 파일을 실행할때만 수행되는 부분.
#import 될 경우에는 실행되지 않는 부분임.

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [string]")
        sys.exit()
    
    seq = sys.argv[1] #명령어에서 실행할 파일명 뒤의 인수를 받아옴
    c1 = comp1(seq) #comp1 함수 호출 test
    c2 = comp2(seq) #comp2 함수 호출 test
    print(seq)
    print(c1)
    print(c2)
