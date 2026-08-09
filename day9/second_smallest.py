a=list(map(int,input("enter the array elements : ").split()))
print(a)
a.sort()
print(a)
new=[]
for i in a:
    if i not in new:
        new.append(i)
new.sort()
if len(new)>1:
    print(f"{new[1]} is second smallest number")
else:
    print("only single value exiest")
'''
1.sort is used to sort the elements in ascending order
2.new  list is used to store the elements without duplicate elements
3.loop is used to add elements into new 
4.if condition used beacause if a list contain the same elements then size will be 1 then printing 2nd index wil throw a error to overrcome that probnlem we used the if condition
'''