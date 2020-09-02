str="This Is graphic Era demmeD to Be University"
u=0
l=0
for i in str:
    if(i!=" "):
        if(i.isupper()):
            u+=1
        else:
            l+=1
print("{} upper case alphabets ".format(u))
print("{} lower case alphabets ".format(l))