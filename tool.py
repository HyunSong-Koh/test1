import sys


#FASTA 클래스
class FASTA:
    #생성자
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.count = {} # count 딕셔너리
        self.length = 0 # length 속성
    
    #method(각 염기 수 count)
    def count_base(self):
        with open(self.file_name, 'r') as handle:
            for line in handle: #for문에 파일객체를 지정하면, 파일 내용을 한 줄씩 읽어 변수에 저장
                if line.startswith(">"):
                    continue
                line = line.strip()
                for s in line:  # line으로 받은 문자열의 문자를 순서로 받아옴.
                    if s in self.count: #count dic안에 key로
                        self.count[s] += 1
                    else:
                        self.count[s] = 1

    def __len__(self):
        length = 0
        for k,v in self.count.items():
           self.length += v
        return self.length

"""
    def len_seq(self):
        length = 0
        for k,v in self.count.items():
           self.length += v
        return self.length
"""

#FASTQ 클래스 (파일의 하나의 리드가 4줄임)
class FASTQ:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.read_num = 0   #리드의 개수
        self.base = {}      #염기의 개수

    def count_read_num(self):
        cnt = 0 # line count
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if cnt % 4 == 0:    #리드의 첫줄이면,
                    header = line.strip()   #헤더임.
                    self.read_num += 1 #리드 수 +1
                elif cnt % 4 == 1:  #리드의 둘째줄,
                    seq = line.strip() #서열
                    for s in seq:
                        if s in self.base:
                            self.base[s] += 1
                        else:
                            self.base[s] = 1
                elif cnt % 4 == 3:  #리드의 넷째줄,
                    qual = line.strip() #퀼리티
                cnt += 1
   

#직접 해당 파일을 실행하면, __name__ == "__main__" 이 참이되어 if문 내용이 수행됨.
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [fasta]")  #
        sys.exit()
    file_name = sys.argv[1]
    #t = FASTA(file_name)
    t = FASTQ(file_name)
    #t.count_base()
    #print(t.len_seq())
    #print(t.count)
    #t.count_read_num()  #count_read_num 메소드 호출
    #print(t.read_num) #read_num 속성의 값 출력
    t.count_read_num()
    print(t.base)



