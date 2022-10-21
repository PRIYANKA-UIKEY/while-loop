n=int(input("enter number......"))
m=5
i=1
while i<=n:
    if n<m:
        print("this number small,try one more time")
    if n>m:
        print("this number great, try one more time")
    elif n==m:
        print("wow you guessed the correct number")
    else:
        ("guessing until all the chance are filled")
    break

