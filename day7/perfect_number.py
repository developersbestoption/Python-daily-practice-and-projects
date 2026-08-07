number=int(input("enter the number :"))
if number<=0:
    print("not a perfect number")
else:
    new=0
    for i in range(1,number):
        if number%i==0:
            new+=i 
    if new == number:
         print("perfect number")
    else:
         print("not a perfect number")
