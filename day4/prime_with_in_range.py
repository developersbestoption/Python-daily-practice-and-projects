#number=int(input("enter the number : "))
'''
1.<=1
2.!itself
is_prime
'''
'''
is_prime=True
if number<=1:
   # print(f"{number} is not prime number")
    is_prime=False 
else:
    for i in range(2,number):
         if number%i==0:
             is_prime=False 
             break 
         
         # else:
             is_prime=True
if is_prime:
    print(f"{number} is prime number")
else:
    print(f"{number}  is not a prime number")'''
start=int(input("enter the start range : "))
end=int(input("enter the end range : "))
is_prime=True 
if start<=1 or end<=1:
    is_prime=False
else:
    for i in range(start ,end+1):
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
if is_prime:
    print("hii")
