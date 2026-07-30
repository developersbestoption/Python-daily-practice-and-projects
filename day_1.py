#day1
print("in this program u will know about a number you entereds")
number = int(input("enter the number :"))
def finder(num):
    last_digit=num%10
    if not last_digit % 2:
        print(f"{num} is divisible by 2")
    sum_of_digits=0
    while True:
        last_digit=num%10
        sum_of_digits += last_digit
        num//=10
        print(last_digit)
        print(sum_of_digits)
        if num==0:
            break
    if not sum_of_digits%3:
        print(f"{num}can be divisible by 3")
    else: 
        print(f"{number} can't be divisible by 3")
    #for knowing the wether is divisible by a 4 or not , last two digits should be divide by 4
    timer=0
    while True:
       # last_digit=num%10
       print(num)
       break
finder(number)
