#p1
'''
a=int(input())
b=int(input())
if a > b:
    print(a)
else:
    print(b)
    '''
#p2
'''
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
     print(a)
elif b>c:
    print(b)
else:
    print(c)
    '''
#p3
'''
a=int(input())
b=int(input())
if a > b:
    print(b)
else:
    print(a)
    '''
#p4
'''
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    a=0
elif b>c:
    b=0
else:
    c=0
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
    '''
#p5 print many hello world  
'''
for i in range (1000):
    print("hello world")    
'''
#p6
'''
a,b=map(int,input().split())
if a==b:
    print("a == b")
elif a>b:
    print("a > b")
else:
    print("a < b")
    '''
#p7
#approach 1
'''
n=int(input())
if n>0:
   res=0
   while n>0:
     r=n%10:
     res=(res*10)+r
     n=n//10
   print(res)
elif n == 0:
   print(n)
else:
   res=0
   n=n*-1
   while n > 0:
     r=n%10
     res=(res*10)+r
     n=n//10
   print(-1*res)
   '''   
#triangle
'''a,b,c=map(int,input().split())
if a+b>c and  b+c>a and c+a>b:
    print("Yes")
else:
    print("No")
'''
#n no of students and k no of fruits
'''
n=int(input())
k=int(input())
i=int(input())
while(i!=0)
'''
#number reverse
#approach -1
'''
n=int(input())
print(str(n)[::-1])
'''
#approach-2
'''
n=int(input())
if n > 0:
    res=0
    while n > 0:
        r=n%10
        res=(res*10)+r
        n=n//10
    print(res)
elif n==0:
    print(n)
else:
    res=0
    n=n*-1
    while n > 0:
        r=n%10
        res=res*10+r
        n=n//10
        print(r*-1)
        '''
#watermelon
#approach-1
'''
w=int(input())
if w > 2 and w%2:
    print("Yes")
else:
    print("No")
    '''
#approach-2
'''
w=int(input())
if w%2==0:
   if w > 2:
     print("Yes")
   else:
     print("No")
   else:
     print("No")
     '''
   
#P9 fever in foreign heat
'''
n=int(input())
while n > 0:
     a=int(input())
     if(a>98):
       print("Yes")
else:
     print("No")
     n=n-1
 '''
#using for
'''n=int(input())
for i in range(n):
     a=int(input())
     if(a>98):
       print("Yes")
else:
     print("No")
    '''
#p10 discount
'''
n=int(input())
for i in range(n):
    a=int(input())
    print(100-n)
    '''

#p11 tv
'''
n= int(input())
for i in range(n):
 a,b,c,d=map(int,input().split())
if a-c>b-d:
     print("second")
elif a-c<b-d:
     print("first")
else:
    print("any")
    '''
#p12 childrens &candies
'''
n=int(input())
for i in range(n):
    n,x=map(int,input().split())
    if n > x:
        k=n - x
        if k%4==0:
            print(k//4)
        else:
            print(k//4+1)
    else:
            print(0)
            '''
#p13 piza
#approach-1
'''
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    ts=n*x
    tp=0
    while ts >=4:
        tp=tp+1
        ts=ts-4
     if tp == 0:
        print(tp)
    else:
        print(tp+1)
        '''
#approach-2
'''
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    k=n*x
if k%4 == 0:
     print(k//4)
else:
     print((k//4)+1)
     '''
                      


