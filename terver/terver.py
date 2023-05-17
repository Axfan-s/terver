import matplotlib.pyplot as plt
from tabulate import tabulate
import random
from collections import Counter

print("Условия задачи")
print("При каждом цикле обзора радиолокатора объект (независимо от других циклов) обнаруживается с вероятностью p. С.в. η — число циклов обзора до обнаружения объекта")
print ("Введите число экспериментов")
n=int(input())
print("Введите вероятность")
p=float(input())
while p>1:
    print("Вероятность не может быть больше единицы")
    print("Введите вероятность")
    p=float(input())
print("Первая часть")
print()
k=0
y=[]
x=[]
r=[]
for i in range(n):
 m=0
 k=0
 while k!=1:
    u=random.random()
    if u<p:
        k=1
    else:
        k=0
    m+=1
 if i==0:
  x.append(1)
 else:
  h=1
  for j in y:
   if m==j:
     h+=1
  x.append(h)
 y.append(m)
#print(y)
#print(x)
for g in (x):
    r.append(g/n)
#print(r)
y1=[]
x1=[]
l=max(y)
for i in range(l+1):
    if i in y:
        y1.append(i)
    else:
        continue
print(y1)
c=Counter(y)
for i in range(len(y1)):
    a=c[y1[i]]
    if a!=0:
        x1.append(a)
    else:
        continue
print (x1)
b=[]
for i in range(len(x1)):
    b.append (x1[i]/n)
print(b)
Table=[]

for i in range(len(y1)):
 Table.append([y1[i],x1[i],b[i]])

print(tabulate(Table,tablefmt="fancy_grid"))

E=1/p
s=0
a=len(y1)
for i in range(len(y1)):
    s+=x1[i]*y1[i]
xcm=s/n 
d=((y1[a-1]-y1[0])**2)/2
Table2=[E, xcm, abs(xcm-E), d, E]
D=(1-p)/(p*p)
s=0
for i in range(a):
    s+=(y1[i]-xcm)**2*x1[i]
S=s/n
R=y1[a-1]-y1[0]
if(a%2==0):
    Me=(y1[a//2-1]+y1[a//2])/2
else:
    Me=y1[(a-1)//2]
print ("Математическое ожидание: ",E)
print("x выборочное среднее: ",xcm)
print("E-x_: ", abs(E-xcm))
print("Дисперсия: ",D)
print("Выборочная дисперсия: ", S)
print("D-S^2: ",abs(S-D))
print("Размах выборки:", R)
print("Выборочная медиана: ",Me)
s=1
ss=[]
z=[]
i=1
o=[0,0]
w=[0,1]
plt.plot(w,o,"b")
plt.plot(w,o,"r")
func=[]
while s>0.001:
    s*=1-p 
    ss=(1-s)
    func.append(ss)
    k=[i,i+1]
    k1=[ss,ss]
    plt.plot(k,k1,"b")
    i+=1
s=0
l=i
pogr=[]
while len(func)<=len(y1):
 func.append(1)
if len(func)>len(b):
    j=len(b)
else:
    j=len(func)
for i in range(len(y1)):

    s+=b[i]
    if i!=len(y1)-1:
     k=[y1[i],y1[i+1]]
    else:
     k=[y1[i],y1[i]+4]
    k1=[s,s]
    pogr.append(abs(func[y1[i]-1]-s))
     
    plt.plot(k,k1,"r")
o=[1.0,1.0]
w=[k[1],l]
print("Наибольшее отклонение функций",max(pogr))
plt.plot(w,o,"r")
w=[]
plt.show()


