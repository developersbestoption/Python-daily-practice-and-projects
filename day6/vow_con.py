a=input("enter the word :")
vow=0
con=0
for i in range(len(a)):
    if a[i].isalpha():
       
       if a[i] in "aeiou" or a[i] in "AEIOU":
           vow+=1
       else:
        con+=1
print("vowels are :", vow)
print("consonents are : ", con)