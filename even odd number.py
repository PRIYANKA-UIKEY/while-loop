a=int(input("enter the number"))
i=10
sum=0
while i<=50:
    if i%2==0:
        sum=sum+i
        print("sum of even number",i,"=",sum)
    if i%2!=0:
        sum=sum+i
        print("sum of odd number",i,"=",sum)
    i=i+1

