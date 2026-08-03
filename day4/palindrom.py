number=int(input("enter the number :"))
number1=number
new_number=0
while True:
    last_digit=number1%10
    new_number+=last_digit
    number1//=10
    if number1 == 0:
        break
    new_number*=10
if new_number == number :
    print(f" {number} is a palindrom ")    
else :
    print(f"{number} is not a palindrom number")
