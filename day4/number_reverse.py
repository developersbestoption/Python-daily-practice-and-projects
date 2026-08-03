number =int(input("enter the number :"))
new_number=0
while True:
    last_digit=number%10
    new_number+=last_digit
    number//=10
    if number==0:
        break
    new_number*=10
print(new_number)