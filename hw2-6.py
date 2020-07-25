# k-mer generation

import sys
"""
k개의 base로 이루어진 서열을 k-mer라고 부름,

숫자 n을 입력받아 n-mer를 생성하는 프로그램.
"""


l1 = ["A","C","G","T"]
l2 = ["A","C","G","T"]

def mer(l1, l2, n):
    if n == 1:
        return l2 

    ltmp = []
    for s1 in l1:
        for s2 in l2:
            ltmp.append(s1+s2)
    return mer(l1, ltmp, n-1)   #재귀
#ex. n = 2일 경우, 리스트 ltmp를 return!

n = int(sys.argv[1]) #파일 실행시 인수로 입력받은 문자 int형으로 받음.

#print(mer(l1,l2,n))


#n-mer의 리스트를 변수 res에 저장.
res = mer(l1,l2,n)

def pal_cnt(list):
    cnt = 0
    for str in list:    #리스트의 문자열 하나씩
        pal_check = 0
        for i in range(len(str)//2):
            if str[i] == str[-(i+1)]:
                continue
            else:
                pal_check += 1
        if pal_check == 0:
            cnt += 1
        else:
            continue
    return cnt

print(f"palindrome의 개수: {pal_cnt(res)}")
    
