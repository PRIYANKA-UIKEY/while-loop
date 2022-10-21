# index=0
# while 1:
#     print(index,"",end="")
#     index=index+1
#     if index==10:
#         break
#     print("found at",index,"location")

a=[12,45,34]
i=0
sum=0
l=[]
while i<len(a):
    k=a[i]%10
    k1=a[i]/10
    k2=a[i]//10
    sum=k+k2
    l.append(sum)
    i=i+1
print(l)



