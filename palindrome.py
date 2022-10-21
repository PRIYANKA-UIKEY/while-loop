n=int(input("enter the number"))
r=0
x=n
while n>0:
    r=r*10+(n%10)
    n=n//10
if x==r:
    print("this is palindrome")
else:
    print("this is not palindrome")






    



    