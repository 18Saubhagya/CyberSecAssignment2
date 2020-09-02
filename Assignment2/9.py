def fibo(n,a,b,i):
    if i==n-1:
        return 
    sum=a+b
    print(sum,end=" ")
    a=b
    b=sum
    fibo(n,a,b,i+1)


n=int(input("Enter the range "))
print(1,end=" ")
fibo(n,0,1,0)