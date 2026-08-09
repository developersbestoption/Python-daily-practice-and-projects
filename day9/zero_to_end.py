a=list(map(int,input("enter array elements :").split()))
new=[]
new2=[]
for i in a:
    if i != 0:
        new.append(i)
    else:
        new2.append(i)
new.extend(new2)
print(new)