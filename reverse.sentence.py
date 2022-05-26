def rev(lst,l):
    if l==0:
        return 
    print(lst[l-1],end=" ")
    rev(lst,l-1)
str="pankaj avin friends"
lst=str.split()
rev(lst,len(lst))
