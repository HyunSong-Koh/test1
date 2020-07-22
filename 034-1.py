l = [3,1,1,2,0,0,2,3,3]

d={}

for elem in l:
    if elem in d:
        d[elem] += 1
    else:
        d[elem] = 1

print(d) #딕셔너리 출력
