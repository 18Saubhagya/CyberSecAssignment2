n=int(input("Enter the range "))
le=[]
to=()
str='Prime'
for i in range(2,n+1):
    for j in range(2,i):
        if (i%j==0):
            str='Non Prime'
            break
        else:
            str='Prime'
    to=(i,str)        
    le.append(to)
    le