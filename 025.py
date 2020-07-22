seq1 = "ATGTTATAG"

for i in range(0,len(seq1),3):
    #print[i] # 0 3 6 
    #print(i,seq1[i]) # 인덱싱

#    for j in range(0,3):
#        print(seq1[i+i], end='')

    print(i, i+3, seq1[i:i+3])
