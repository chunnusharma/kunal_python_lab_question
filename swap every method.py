num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
temp=num1
num1=num2
num2=temp
print("the first number after the swap is:%d"%num1)
print("the second number after the swap is:%d"%num2)
#without third variable-------------------------------------->
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num1,num2=num2,num1
print("the first number after the swap is:%d"%num1)
print("the second number after the swap is:%d"%num2)
#swap using arthimetic operator----------------------------->
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num1=num1*num2
num2=num1/num2
num1=num1/num2
print("the first number after the swap is:%d"%num1)
print("the second number after the swap is:%d"%num2)
#swap using bitwise opertors-------------------------------->
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num1=num1^num2
num2=num1^num2
num1=num1^num2
print("the first number after the swap is:%d"%num1)
print("the second number after the swap is:%d"%num2)
