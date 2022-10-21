n=int(input("enter the number...."))
i=1
while n>0:
    i=i*(n%10)
    n=n//10
print("product of digit number",i)
i=i+1
    
