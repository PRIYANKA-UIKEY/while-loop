a=int(input("enter the number..."))
i=0
while a>0:
    i=i*10+(a%10)
    a=a//10
print(i)
