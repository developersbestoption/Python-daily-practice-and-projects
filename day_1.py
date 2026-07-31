#day1
print("in this program u will know about a number you entereds")
number = int(input("enter the number :"))
def finder(num):
    num=num
    #---------checking  number divisibility of 2(last digit should divisible by 2)
    last_digit=num%10
    if not last_digit % 2:
        print(f"{num} is divisible by 2")
    else:
        print(f"{num} can't be divisible by 2")
    #--------checking  number divisibility of 3(sum of all digits of a number should be divisible by 3)
    sum_of_digits=0
    num1=num
    while True:
        last_digit=num1%10
        sum_of_digits += last_digit
        num1//=10
        #print(last_digit)
        #print(sum_of_digits)
        if num1==0:
            break
    if not sum_of_digits%3:
        print(f"{number}can be divisible by 3")
    else: 
        print(f"{number} can't be divisible by 3")
    #-------for knowing the wether is divisible by a 4 or not , last two digits should be divide by 4
    count=0
    sum_of_last_two_digits=0
    print(num1)
    while True:
       #last_digit=num%10
       print(num)
       break
finder(number)
