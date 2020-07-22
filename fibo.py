#피보나치 수열

#방법1
"""
n = int(input("input n: "))
fn = []
for i in range(n+1):
    if i == 0:
        fn.append(i)
    elif i == 1:
        fn.append(i)
    elif i>=2:
        fn.append(fn[i-1]+fn[i-2])

print(fn[n])

"""

#방법2
import sys

def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(sys.argv[1]) # 인수로 숫자를 받기 위함.

print(fib(n))

#ex. python fibo.py [숫자]

