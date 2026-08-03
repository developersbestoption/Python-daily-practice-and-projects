number=int(input("enter number :"))
number1 =number
count=0
while True:
    count+=1
    number//=10
    if number==0:
        break
print(f"{number1} consist of {count} digits")
