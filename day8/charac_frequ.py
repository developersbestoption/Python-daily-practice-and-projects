a=input("ebter the word : ")
seen=" "
for i in range(len(a)):
        if a[i] in seen:
            continue
        print(f"{a[i]} : {a.count(a[i])}")
        seen+=a[i]
