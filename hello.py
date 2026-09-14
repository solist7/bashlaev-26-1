##print('hello world')
##a = 10
##b = 24
##res = a + b 
##print('result',res)
a,b=int(input()),int(input())
if a < 0 and b < 0 :
    print(min(a,b))
else:
    print('>0')
res = a+b
if res %3==0 and res%5==0:
    print('YES')
    