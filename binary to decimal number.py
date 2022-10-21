n=int(input("enter the number"))
sum=0
i=0
while n!=0:
    r=n%10
    sum =sum+r*pow(2,i)
    n=int(n/10)
    i=i+1
print("decimal number",sum)


