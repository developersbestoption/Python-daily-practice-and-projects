num=int(input("enter the number"))
print(f"original number : {num}")
new_num=0
while  True:
    last_digit=num%10 
    new_num+=last_digit
    num//=10
    if num==0:
       break
    new_num*=10
print(f"new number {new_num}")     
'''
345
n=5
34
n*10
50
'''