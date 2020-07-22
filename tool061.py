import sys

class FASTQ:
    def __init__ (self, file_name: str):
        self.file_name = file_name
    
    def cnt_lead(self):
        lead_cnt = 0
        with open(self.file_name, 'r') as handle:
            for lineNum in range(len(handle)):
                lead_cnt += 1
        print(lead_cnt)


if __name__ == "__main__":
    
