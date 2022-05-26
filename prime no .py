num=int(input())
for i in range(1,(num//2)+2):
    if (num%i)==0:
        print('not prime')
        break
    else:
        print('prime')
