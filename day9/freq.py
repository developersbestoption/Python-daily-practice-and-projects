a=list(map(int,input("enter the array elements :").split()))
seen=[]
for i in a:
    if i in  seen:
        continue
    print(i ,a.count(i))
    seen.append(i)
'''finding the frequency of a elements in array'''