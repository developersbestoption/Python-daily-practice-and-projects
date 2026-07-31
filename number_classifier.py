class Main:
   def __init__(self):
    print("hello")
        #---------checking  number divisibility of 2(last digit should divisible by 2)
   def div_2(self,num):
    last_digit=num%10
    if not last_digit % 2:
        print(f"{num} can be divisible by 2")
    else:
       print(f"{num} can't be divisible by 2")
         #--------checking  number divisibility of 3(sum of all digits of a number should be divisible by 3)
   def div_3(self,num):
       sum_of_digits=0
       number=num
       while True:
           last_digit=num%10
           sum_of_digits += last_digit
           num//=10
           #print(last_digit)
           #print(sum_of_digits)
           if num==0:
               break
       if not sum_of_digits%3:
           print(f"{number} can be divisible by 3")
       else: 
           print(f"{number} can't be divisible by 3")
     #-------for knowing the wether is divisible by a 4 or not , last two digits should be divide by 4
   def div_4(self,num):
          count=0
          number=num
          sum_of_last_two_digits=0
          while count<=2:
             last_digit=num%10
             sum_of_last_two_digits+=last_digit
             count+=1
          if not sum_of_last_two_digits % 4 :
              print(f"{number} can be divisible by 4")
          else:
              print(f"{number} can't be divisible by 4")
   def div_5(self,num):
       if num%10 == 0 or num%10 ==1 :
            print(f"{num} can be divisible by 5")
       else:
            print(f"{num} can't be divisible by 5")

       
       



a=Main()
number = int(input("enter the number :"))
a.div_2(number)
a.div_3(number)
a.div_4(number)
a.div_5(number)