a=input("enter the sentence :")
words=a.split()#this splits the sentence and make list of words
for i in words:#this takes each word into a i and we perform the revesing by indexing 
    print(i[::-1],end=" ")# we use "end" to continue in the same line