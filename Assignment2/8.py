n=int(input("Enter the limit "))
dl={}
dl[2]="Prime"
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
            dl[i]='Non prime'
            break
        else:
            dl[i]='prime'
dl