l = [3,1,1,2,0,0,2,3,3]
max = l[0]
min = l[0]
for i in l:
    if max<l[i]:
        max = l[i]
    if min>l[i]:
        min = l[i]
print(f"max: {max}")
print(f"min: {min}")
