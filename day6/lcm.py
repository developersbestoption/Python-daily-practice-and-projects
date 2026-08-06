a=int(input("enter first number : "))
b=int(input("enter second number : "))
i=1
while True:
    if(i%a==0 and i%b==0):
        print("lcm :",i)
        break
    i+=1 

