number =int(input("enter number :"))
number1=number
new_number=0
while True :
    last_digit=number1%10
    new_number+=last_digit
    if number1==0:
        break
    number1//=10
print(f"sum of {number} digits are {new_number}")