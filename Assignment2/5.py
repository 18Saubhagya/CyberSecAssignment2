def product(list):
    res=1
    for i in list:
        res*=i
    return res    


list=[1,2,3,4,5,6,7]
print(product(list))