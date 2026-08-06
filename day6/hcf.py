a=int(input("enter the first number :"))
b=int(input("enter the second number : "))
for i in range(b,1,-1):
    if a%i==0 and b%i==0:
        print(i,"is the hcf ")
        break
