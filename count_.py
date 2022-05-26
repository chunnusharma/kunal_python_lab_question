f=open('avin.txt','r')
s=n=t=0
str=f.read()
for i in str:
    if ord(i)==32:
        s+=1
    elif i=='\n':
        n+=1
    elif i=='\t':
        t+=1
print(s,n,t)
f.close()
