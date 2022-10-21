i=0
rev=0
while i<=50:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count+=1
        j=j+1
    if count==2:
        i=i*10+(rev%10)
        rev=rev//10
       
        print(i)
    i=i+1