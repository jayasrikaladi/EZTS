#pass by reference
'''
def myfun(x):
    x[0]=20
lst=[10,11,12,13,14,15]
myfun(lst)
print(lst)
'''

#R-sugarcane juice business
#approach-1
'''
t=int(input())
for i in range(t):
    n=int(input())
    x=int((n*50) - ((0.7)*(n*50)))
    print(x)
'''
#approach- 2
'''t=int(input())
def profit(n):
    x=((n*50)-((0.7)*(n*50)))
    return x
def test(t):
    if t > 0:
       n=int(input())
       print(profit(n))
    else:
       return
    test(t-1)
test(t)
    '''
#watching movie at 2x
'''x,y=map(int,input().split())
k=x-y
k1=k+(y//2)
print(k1)
'''
#using function
'''
def movie(x,y):
    print((x-y)+(y//2))
a,b=map(int,input().split())
def movie(a,b)
'''

#find no of 4
#approach -1
'''
t=int(input())
for i in range(t):
    n=int(input())
    c=0
    while n>0:
      if n%10 == 4:
           c=c+1
      n=n//10
    print(c)
    '''
#approach 2
'''

t=int(input())
def count(n):
    c=0
    while n>0:
       if n%10==4:
           c=c+1
           n=n//10
           return c    
def test(t):
    if t > 0:
        n=int(input())
        print(count(n))
    else:
        retuen
    test(t-1)
test(t)
'''
#factorial
#approach-1
'''
n=int(input())
r=1
for i in range(1,n+1):
    r=r*i
    print(r)
    '''
#approach-2
'''
n=int(input())
r=1
while n > 0:
  r = r * n
  n = n - 1
print(r)
'''
#approach-3

def fact(n):
    if n==0 or n==1:
         return 1
    else:
         return n*fact(n-1)
k=int(input())
print(fact(k))


#next even integer
'''
n=int(input())
if n%2==0:
   print(n+2)
else:
   print(n+1)
   '''
   
#append three
'''
n=int(input())
def temp(n):
    r=n
    c=0
    while r>0:
        c+=1
        r=r//10
    n=(3*pow(10,c))+n
    n=n*10+3
    return n
print(temp(n))
'''



            




