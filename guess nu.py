
guess=int(input("enter guess number...."))
i=0
chance=5
while i<=5:
    n=int(input("enter number"))
    if n==guess:
        print("priyanka,you have won")
        break
    else:
        print("you  have chance")   
    i=i+1
    chance=chance-1
    print(chance)


