import sys

if len(sys.argv) != 2:  #인수가 '실행파일', 'open할 파일' 두개가 아닐경우
    print(f"usage: python {sys.argv[0]} [txt]")
    sys.exit()
fileName = sys.argv[1]

try:
    with open(fileName, 'r') as handle:
        read = handle.readlines() #read는 각 라인을 원소로 하는 리스트

except FileNotFoundError:   #인수로 입력한 file이 없으면 error메시지 출력
    print(f"{f} not found// please check..")
    sys.exit()

print(read) #read 리스트 출력


