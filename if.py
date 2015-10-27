#!/usr/bin/env python
# coding=utf-8
a=3
if a >4:
    print "a>4"
else:
    print "a<4"

a<4
if a >4:
    print "a>4"
elif a<4:
    print "a<4"
else:
    print "a=4"

print "##########"
m=["canglaoshi",["malixia","canglaoshi2"],1]
for i in m:
    print i
print "##########"
for i in range(len(m)):
    print i
    print m[i]

print range(0,9,2)

for n in range(1,100):
    if n%3==0:
        print n
        
print range(3,100,3)
print range(0,100,3)
d={"name":"qiwei","lang":"Python"}
print d.keys()
for k in d.keys():
    print k


c=[1,2,3]
d=[9,8,7]
print zip(c,d)
d=[9,8,7,6]
e=[]
for i in range(len(c)):
    e.append(c[i]+c[i])
m=[]
for x,y in zip(c,d):
    m.append(x+y)
print m
r=[(1,2),(3,4),(5,6)]
print zip(*r)
my={"namethon":"roy","lang":"python"}
infor={}
for k,v in my.items():
    infor[v]=k
print infor

print dict(zip(my.values(),my.keys()))
print dict([(1,2),(3,4)])
week=["sumday",'monday','friday']
for i in range(len(week)):
    print week[i]+"--->"+str(i)
for (i,day) in enumerate(week):
    print day+"--->"+str(i)
r="do you love Canglaoshi? Canglaoshi is a good teacher"
r.split(" ") #这个出来的第一个“canglaoshi有问号”
r.split("?")
r=["Canglaoshi","you","Canglaoshi"]
for i,st in enumerate(r):
    if st=="Canglaoshi": r[i]="PHP"
print r
p2=[]
for i in range(1,10):
    p2.append(i**2)
print p2
p3=[x**2 for x in range(1,10)]
print p3
mm=[' aa','b  b ','   c  c']
print [word.strip() for word in mm]
print [x**2 for x in range(1,10) if x>5]
[x**2 for x in range(1,10) if x>5]
print x
f=open("test.txt")
for lin in f:
   print lin
g=open("test.txt")
for lin in g:
    print lin,
f.close
g.close
dir(f)
m=open("kk.txt",'w')
m.write("Jinlaoshi")
#for i in m:
#    print i,
m.close
with open("kk.txt") as f:
    for i in f:
        print i
import time
import os
import fileinput
#for line in fileinput.input("7562.csv"):
#    print line,
lst=[1,2,3]
n=iter(lst)
print n.next()
f=open("test.txt")
print f.next()

def add_add(a,d):
    """
        注释
       add
       """
    c=a+d
    return c
r=add_add(2,3)
print r

def return_add():
    a=3
    b=9
    return a,b

c=return_add()
print c

