a=input("enter the word : ")
for i in range(len(a)):
    if(a.count(a[i])==1):
        print(a[i])
        break
