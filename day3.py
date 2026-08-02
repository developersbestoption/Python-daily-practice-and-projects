#checking wether given number is palindrom or not
number=int(input("enter the number :"))
number1=number
new_number=0
while True:
    last_digit=number%10
    new_number+=last_digit
    number//=10
    if number==0:
                break
    new_number*=10

print(f" new number {new_number}")
if new_number==number1:
        print(f"{number1} is palindrom number")
else:
        print(f"{number1} is not a palindrom number")