Seq1 = "AGTTTATAG"

for i in range(0,len(Seq1),1):
    if Seq1[i:i+2] == "TT":
        print("index:", i, Seq1[i:i+2])
